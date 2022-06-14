import fastapi_slack
from fastapi import FastAPI, Depends

app = FastAPI()
app.include_router(fastapi_slack.router)


# TODO how to actually set the fastapi-slack settings?
# Probably can be done through env variable


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/slash-commands")
def process_commands(slash_command: fastapi_slack.SlashCommand = Depends()):
    return {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{slash_command.command=} {slash_command.channel_name=} {slash_command.text=}*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hardcoded text YIHAAA"
                }
            }
        ]
    }