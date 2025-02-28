from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from upload.tasks import process_upload

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file = request.FILES['file']
        file_path = f'/tmp/{file.name}'
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        process_upload.delay(file_path)
        return Response({"message": "File uploaded successfully!"})

