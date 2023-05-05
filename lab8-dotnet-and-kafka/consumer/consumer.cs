using Confluent.Kafka;
using System;
using System.Threading;
using Microsoft.Extensions.Configuration;

class Consumer {

    static void Main(string[] args)
    {
        var config = new ConsumerConfig {
                            BootstrapServers = "localhost:29092,localhost:29093,localhost:29094", 
                            ClientId = "dotnet-consumer",
                            };
        config.GroupId = "dotnet-kafka-consumer";
        config.AutoOffsetReset = AutoOffsetReset.Earliest;
        config.EnableAutoCommit = true;


        const string topic = "test-topic";

        CancellationTokenSource cts = new CancellationTokenSource();
        Console.CancelKeyPress += (_, e) => {
            e.Cancel = true; // prevent the process from terminating.
            cts.Cancel();
        };

        using (var consumer = new ConsumerBuilder<string, string>(config).Build())
        {
            consumer.Subscribe(topic);
            try {
                while (true) {
                    var cr = consumer.Consume(cts.Token);
                    Console.WriteLine($"Consumed event from topic {topic} with key {cr.Message.Key,-10} and value {cr.Message.Value}");
                }
            }
            catch (OperationCanceledException) {
                // Ctrl-C was pressed.
            }
            finally{
                consumer.Close();
            }
        }
    }
}