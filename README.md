# bigcode/tiny_starcoder_py COG

Attempt at creating a cog wrapper for [bigcode/tiny_starcoder_py](https://huggingface.co/bigcode/tiny_starcoder_py).

## Run

`cog build -t tiny-starcoder`

`docker run -d -p 5000:5000 --gpus all tiny-starcoder`

## Test

### Input

`curl http://localhost:5000/predictions -X POST -H 'Content-Type: application/json' -d '{"input": {"prompt":"def print_hello_world():"}}'`

### Output

`{"input":{"prompt":"def print_hello_world():","max_new_tokens":20},"output":"def print_hello_world():\n    print(\"Hello World!\")\n\n\ndef print_hello_world_with_args():\n   ","id":null,"version":null,"created_at":null,"started_at":"2023-06-25T03:11:53.088704+00:00","completed_at":"2023-06-25T03:11:54.356038+00:00","logs":"","error":null,"status":"succeeded","metrics":{"predict_time":1.267334},"output_file_prefix":null,"webhook":null,"webhook_events_filter":["completed","start","output","logs"]}`
