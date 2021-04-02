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


FLOWS = {
    "project": {
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
    }
}
MINIMUM_COMMAND_LINE_ARGS = 1
FLOW_NAME = 0
FIRST_FLOW_PARAM = 1
SCRIPT_NAME = 0


def exit_program(message=None):
    if message:
        logging.error(message)
    logging.info(execute_flow.__doc__)
    sys.exit(1)


def execute_flow(user_input):
    """Usage: 
    Basic structure: python3 main.py <FLOW> <FLOW_ARGUMENTS>
    Create a new project: python3 main.py project <PROJECT_NAME>
    Create a new blog post: python3 main.py post <POST_NAME> <POST_CATEGORY> <PROJECT_NAME>
    """

    if (len(user_input) < MINIMUM_COMMAND_LINE_ARGS or not 
        FLOWS.get(user_input[FLOW_NAME])):
        exit_program("The flow does not exist or there is not enough params to process")
    
    if user_input[FLOW_NAME] == 'help':
        exit_program()
    
    flow = FLOWS.get(user_input[FLOW_NAME])
    flow_arguments = user_input[FIRST_FLOW_PARAM: ]
    processor = flow['processor']
    
    if len(flow_arguments) != len(flow.get('arguments')):
        exit_program("Too much arguments")
    
    for index, required_argument in enumerate(flow['arguments']):
        if not user_input[index + FLOW_NAME].strip():
            exit_program("There's an invalid argument")    
    
    processor(flow_arguments)
    processor.process()


if __name__ == "__main__":
    flow_name = 1
    execute_flow(sys.argv[flow_name: ])