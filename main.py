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
    "new_project": {
        "arguments": [
            "project_name"
        ],
        "processor": core.Project
    },
    "new_post": {
        "arguments": [
            "post_name",
            "post_category",
            "project_name"
        ],
        "processor": core.Post
    },
    "help": {
        "arguments": [],
        "processor": logging.info
    }
}
MINIMUM_COMMAND_LINE_ARGS = 1
FLOW_POSITION = 1
SCRIPT_NAME = 1

def exit_program(invalid_arguments_message):
    logging.error(invalid_arguments_message)
    logging.info(process_flow.__doc__)
    sys.exit(1)


def process_flow(user_input):
    """Usage: 
    Basic structure: python3 main.py <FLOW> <FLOW_ARGUMENTS>
    Create a new project: python3 main.py new <PROJECT_NAME>
    Create a new blog post: python3 main.py post <POST_NAME> <POST_CATEGORY> <PROJECT_NAME>
    """
    
    if (len(user_input) -SCRIPT_NAME < MINIMUM_COMMAND_LINE_ARGS or 
            not AVAILABLE_FLOWS.get(user_input[FLOW_POSITION])):
        exit_program("The flow does not exist or there is not enough params to process")
    
    flow = AVAILABLE_FLOWS.get(user_input[FLOW_POSITION].lower())
    
    if len(user_input) -(FLOW_POSITION + SCRIPT_NAME) != len(flow.get('arguments')):
        exit_program("Invalid amount of arguments...")
    
    for index, required_argument in enumerate(flow['arguments']):
        if not user_input[index + (FLOW_POSITION + SCRIPT_NAME)].strip():
            exit_program("There's an invalid argument")
    
    flow_params = user_input[(FLOW_POSITION + SCRIPT_NAME): ]
    processor = flow['processor']
    
    if user_input[FLOW_POSITION].lower() == 'help':
        flow_params = process_flow.__doc__
    
    processor(flow_params)


if __name__ == "__main__":
    process_flow(sys.argv)