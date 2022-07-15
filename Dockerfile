#dockerfile MODELSERVING
FROM pytorch/torchserve:latest-gpu

EXPOSE 8080
EXPOSE 8081
EXPOSE 8082
EXPOSE 7070
EXPOSE 7071

#TorchServe uses default ports 8080 / 8081 / 8082 for REST based inference, management & metrics APIs and 7070 / 7071 for gRPC APIs

ENV gpus='"all"'

#COPY /model/resnet-152-batch_v2.mar model-store/
COPY /model/densenet161.mar model-store/
COPY config.properties config.properties 
CMD ["torchserve", "--start" ,"--ncs","--model-store", "model-store" ,"--models" ,"densenet=densenet161.mar"]
# /home/model-server is working directory into container
