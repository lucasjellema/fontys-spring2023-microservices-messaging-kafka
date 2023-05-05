# .NET / C# and Kafka

https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-install-script

wget https://dot.net/v1/dotnet-install.sh
chmod +x dotnet-install.sh 
./dotnet-install.sh 
echo 'export DOTNET_ROOT=$HOME/.dotnet' >> ~/.bashrc
echo 'export PATH=$PATH:$DOTNET_ROOT:$DOTNET_ROOT/tools' >> ~/.bashrc


In directory producer:

dotnet build producer.csproj

dotnet run

## Consumer

dotnet build producer.csproj

dotnet run


# resources
[Getting Started with Apache Kafka and .NET](https://developer.confluent.io/get-started/dotnet/)