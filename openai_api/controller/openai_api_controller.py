from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from openai_api.controller.request_form.openai_api_request_form import OpenaiApiRequestForm
from openai_api.service.openai_api_service_impl import OpenaiApiServiceImpl


openaiApiRouter = APIRouter()

async def injectOpenaiApiService() -> OpenaiApiServiceImpl:
    return OpenaiApiServiceImpl()

@openaiApiRouter.get('/openai-api')
async def requestOpenaiApiResult(openaiApiRequestForm: OpenaiApiRequestForm,
                                 oepnaiApiService: OpenaiApiServiceImpl =
                                 Depends(injectOpenaiApiService)):

    generatedText = await oepnaiApiService.chatWithGpt(openaiApiRequestForm.userSendMessage)

    return JSONResponse(content=generatedText, status_code=status.HTTP_200_OK)
