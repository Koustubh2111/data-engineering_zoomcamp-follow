from parameterizing_flow import etl_parent_flow
from prefect.docker import DockerImage

docker_image = DockerImage(
                name="ksudar2111/prefectw2",
                tag="zoomcamp",
                dockerfile="Dockerfile"
                        )


"""
deploy method builds and pushes the image to registry to use. 
Push and build parameters can be set to False, but unable to use a docker image already from registry - authentication error!
"""

if __name__ == "__main__":
    etl_parent_flow.deploy(
        name = 'docker-deploy-first-w2',
        work_pool_name = 'docker-deploy-work-pool-w2',
        image = docker_image,
        schedule = None,
        parameters={
            'color':'green',
            'year' : 2021,
            'months' : [3,4,5],
            'tables' : [f'rides_21_{m}' for m in [3,4,5]]
            }
    )

