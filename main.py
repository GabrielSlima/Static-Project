import core
import sys
import json
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)

AVAILABLE_FLOWS = {
    "new": {
        "arguments": [
            "project_name"
        ],
        "processor": core.Project
    },
    "post": {
        "arguments": [
            "post_name",
            "post_category",
            "project_name"
        ],
        "processor": core.Post
    },
    "help": {
        "arguments": [],
        "processor": help 
    }
}
MINIMUM_COMMAND_LINE_ARGS = 1
FLOW_POSITION = 1
SCRIPT_NAME = 1

def exit_program():
    invalid_arguments_message = "Invalid arguments..."
    logging.error(invalid_arguments_message)
    help()
    sys.exit(1)

def handler(user_input):
    if (len(user_input) -SCRIPT_NAME < MINIMUM_COMMAND_LINE_ARGS or 
            not AVAILABLE_FLOWS.get(user_input[FLOW_POSITION])):
        exit_program()
        
    if len(user_input) -SCRIPT_NAME != len(AVAILABLE_FLOWS.get(user_input[FLOW_POSITION])):
        exit_program()

    flow = AVAILABLE_FLOWS[user_input[FLOW_POSITION]]
    for index, required_argument in enumerate(flow['arguments']):
        if not user_input[index + (FLOW_POSITION + SCRIPT_NAME)].strip():
            exit_program()

    processor = flow['processor']
    processor(user_input[(FLOW_POSITION + SCRIPT_NAME): ])

def help():
    """Usage: 
    Basic structure: python3 main.py <FLOW> <FLOW_ARGUMENTS>
    Create a new project: python3 main.py new <PROJECT_NAME>
    Create a new blog post: python3 main.py post <POST_NAME> <POST_CATEGORY> <PROJECT_NAME>
    """
    logging.info(help.__doc__)

if __name__ == "__main__":
    handler(sys.argv)