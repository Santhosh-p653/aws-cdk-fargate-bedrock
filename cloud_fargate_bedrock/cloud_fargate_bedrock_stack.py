from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
)

from constructs import Construct


class CloudFargateBedrockStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # -----------------------------
        # VPC
        # -----------------------------
        vpc = ec2.Vpc(
            self,
            "CloudVpc",
            max_azs=2
        )

        # -----------------------------
        # ECS Cluster
        # -----------------------------
        cluster = ecs.Cluster(
            self,
            "CloudCluster",
            vpc=vpc
        )

        # -----------------------------
        # Amazon ECR Repository
        # -----------------------------
        repository = ecr.Repository(
            self,
            "CloudFargateBedrockRepository",
            repository_name="cloud-fargate-bedrock",
            removal_policy=RemovalPolicy.DESTROY,
            empty_on_delete=True,
        )

        # Outputs for verification
        self.cluster = cluster
        self.repository = repository