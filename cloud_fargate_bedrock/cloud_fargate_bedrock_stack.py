from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_logs as logs,
    aws_iam as iam,
)
from constructs import Construct


class CloudFargateBedrockStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        vpc = ec2.Vpc(
            self,
            "CloudVpc",
            max_azs=2
        )

        # ECS Cluster
        cluster = ecs.Cluster(
            self,
            "CloudCluster",
            vpc=vpc
        )

        # ECR Repository
        repository = ecr.Repository(
            self,
            "CloudRepository",
            repository_name="cloud-fargate-bedrock",
            removal_policy=RemovalPolicy.DESTROY,
            empty_on_delete=True,
        )

        # CloudWatch Log Group
        log_group = logs.LogGroup(
            self,
            "CloudLogs",
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Fargate Task Definition
        task_definition = ecs.FargateTaskDefinition(
            self,
            "CloudTask",
            cpu=256,
            memory_limit_mib=512,
        )

        # Allow Bedrock access
        task_definition.task_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "bedrock:InvokeModel",
                    "bedrock:InvokeModelWithResponseStream",
                ],
                resources=["*"],
            )
        )

        # Container
        container = task_definition.add_container(
            "CloudContainer",
            image=ecs.ContainerImage.from_ecr_repository(
                repository,
                tag="latest",
            ),
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix="cloud",
                log_group=log_group,
            ),
        )

        # Flask runs on port 5000
        container.add_port_mappings(
            ecs.PortMapping(
                container_port=5000
            )
        )

        # ECS Fargate Service
        ecs.FargateService(
            self,
            "CloudService",
            cluster=cluster,
            task_definition=task_definition,
            desired_count=1,
            assign_public_ip=True,
        )