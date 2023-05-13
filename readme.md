# SK-Learn-Image-FastAPI

## Deploy with Docker

Build image

    docker build --network=host -t sk-learn-image:v0 .

Run Docker

    docker run --name sk-learn-image -p 8009:8009 -d sk-learn-image:v0

send the image file in a request:

    curl -X POST -F file=@keli.jpg http://localhost:8009/predict

## Benchmarking with Apache Bench

Remove Docker:

    docker stop sk-learn-image
    docker rm sk-learn-image

Run Benchmark Code:

    docker run --name pytorch_flask -p 8009:8009 -d sk-learn-image:v0 python benchmark.py

Benchmarking:

    ab -n 100 -c 10  http://localhost:8009/predict

## License

License: BSD 3 clause
