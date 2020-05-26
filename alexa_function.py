# -*- coding: utf-8 -*-

import random
import logging
import requests

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

##Skil info
SKILL_NAME = "McKenzie House"
GET_FACT_MESSAGE = "I would say: "
HELP_MESSAGE = "You can say tell me a mckenzie fact, or, you can say stop... What can I help you with?"
HELP_REPROMPT = "What can I help you with?"
STOP_MESSAGE = "Goodbye!"
FALLBACK_MESSAGE = "The McKenzie House skill can't help you with that. What can I help you with?"
FALLBACK_REPROMPT = 'What can I help you with?'
EXCEPTION_MESSAGE = "Sorry. I cannot help you with that."


data = [
  'Test fact in python'
]

map_data = {
    "mom": "Mom loves bowls",
    "dad": "Dad loves cars",
    "kelsey": "Kelsey smells",
    "keenan": "Keenan is the best",
    "kam": "Kamryn is a nerd",
    "cam": "Kamryn is a nerd",
    "ro": "Rossella is lovely",
    "rossella": "Rossella is lovely"
}


sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Intent handlers
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input))
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LaunchRequestHandler")

        speech = "Welcome to McKenzie House!"

        handler_input.response_builder.speak(speech).ask(
            HELP_REPROMPT).set_card(
            SimpleCard(SKILL_NAME, speech))
        return handler_input.response_builder.response

class GetNewFactHandler(AbstractRequestHandler):
    """Handler for GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("GetNewFactIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewFactHandler")

        random_fact = random.choice(data)
        speech = GET_FACT_MESSAGE + random_fact

        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(SKILL_NAME, random_fact))
        return handler_input.response_builder.response
        
class GetSpecificFactHandler(AbstractRequestHandler):
    """Handler for GetSpecificFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("GetSpecificFactIntent")(handler_input))
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetSpecificFactHandler")
        slots = handler_input.request_envelope.request.intent.slots
        logger.info(slots)
        person = slots['person']
        
        logger.info(person)
        name = person.value
        specific_fact = map_data[name]
        speech = GET_FACT_MESSAGE + specific_fact
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(SKILL_NAME, specific_fact))
        return handler_input.response_builder.response

class GetApiRequestHandler(AbstractRequestHandler):
    """Handler for GetApiRequestIntent."""
    def can_handle(self, handler_input):
        return (is_intent_name("GetApiRequestIntent")(handler_input))
    
    def handle(self, handler_input):
        logger.info("In API handler")
        item_names = ""
        url = "http://fridge.mckenzie-house.com/api/items"
        response = requests.get(url)
        if response.status_code == 200:
            items = response.json()
        
        for item in items:
            item_names = item_names + item['name']+", "
        speech = item_names
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(SKILL_NAME, "Items"))
        return handler_input.response_builder.response
            


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        handler_input.response_builder.speak(HELP_MESSAGE).ask(
            HELP_REPROMPT).set_card(SimpleCard(
                SKILL_NAME, HELP_MESSAGE))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(STOP_MESSAGE)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(FALLBACK_MESSAGE).ask(
            FALLBACK_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(
            HELP_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetNewFactHandler())
sb.add_request_handler(GetSpecificFactHandler())
sb.add_request_handler(GetApiRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
# sb.add_global_request_interceptor(RequestLogger())
# sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()

## UTILS

def http_get(url, path_params=None):
    """Return a response JSON for a GET call from `request`."""
    # type: (str, Dict) -> Dict
    response = requests.get(url=url, params=path_params)

    if response.status_code < 200 or response.status_code >= 300:
        response.raise_for_status()
    return response.json()

