echo "Checking if docker is installed"
if ! [ -x "$(command -v docker)" ]; then
    echo "Install and start docker"
    yum update -y
    yum install -y docker
    service docker start
    usermod -a -G docker ec2-user
    echo "Done..."
else
    echo 'Docker is installed'
fi

docker image build -t press-img .

docker stop press-container
docker rm press-container

docker run -d --name press-container -p 80:5000 press-img
