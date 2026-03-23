from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id):
        self.stream_id = stream_id
        self.type = None
        self.processed_data = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        filtered_batch = []
        for element in data_batch:
            if criteria in element:
                filtered_batch.append(element)
        return filtered_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
    

class SensorStream(DataStream):
    def __init__(self):
        self.avg_temp = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.type = "Environmental Data"
        values = []
        try:
            for element in data_batch:
                values.append(float(element.split(':')[1]))
        except ValueError:
            raise ValueError("invalid data")

        total_temp = 0
        self.processed_data = 0
        for value in values:
            total_temp += value
            self.processed_data += 1
        self.avg_temp = total_temp / self.processed_data
        readings_label = "reading" if self.processed_data <= 1 else "readings"

        return ("Sensor analysis: "
                f"{self.processed_data} {readings_label} processed, "
                f"avg temp: {self.avg_temp}°C")


class TransactionStream(DataStream):
    def __init__(self):
        self.net_flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.type = "Financial Data"
        values = []
        try:
            for element in data_batch:
                action, value = element.split(':')
                if action == "sell":
                    values.append(- int(value))
                elif action == "buy":
                    values.append(int(value))
                else:
                    pass
        except ValueError:
            raise ValueError("invalid data")

        self.net_flow = 0
        self.processed_data = 0
        for value in values:
            self.net_flow += value
            self.processed_data += 1
        op_label = "operation" if self.processed_data <= 1 else "operartions"
        net_flow_prefix = "+" if self.net_flow >= 0 else "-"
        value = abs(self.net_flow)
        units_label = "unit" if self.net_flow in [-1, 0, 1] else "units"

        return (f"Transaction analysis: {self.processed_data} {op_label}, "
                f"net flow: {net_flow_prefix}{value} {units_label}")


class EventStream(DataStream):
    def __init__(self):
        self.errors_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.type = "System Events"
        for element in data_batch:
            if not isinstance(element, str):
                raise ValueError("invalid data")
            if element not in ["login", "logout", "error"]:
                raise ValueError("unknown event")

        self.errors_count = 0
        self.processed_data = 0
        for element in data_batch:
            if element == "error":
                self.errors_count += 1
            self.processed_data += 1
        errors_label = "error" if self.errors_count in [0, 1] else "errors"
        events_label = "event" if self.processed_data <= 1 else "events"

        return (f"Event analysis: {self.processed_data} {events_label}, "
                f"{self.errors_count} {errors_label}")


class StreamProcessor():
    def __init__(self):
        self.streams = []

    def add_stream(self, new_stream):
        self.streams.append(new_stream)

    def run_all(self, data_batches):
        i = 0
        for stream in self.streams:
            if isinstance(stream, SensorStream):
                stream.filter_data(data_batches[i], "temp:")
            stream.process_batch(data_batches)
            i += 1


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    try:
        print("\nInitializing Sensor Stream...")
        sensor = SensorStream("SENSOR_001")
        sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
        data_label = ""
        i = 0
        for data in sensor_data:
            data_label += data
            i += 1
            if i < len(sensor_data):
                data_label += ", "
        filtered_data = sensor.filter_data(sensor_data, "temp:")
        result = sensor.process_batch(filtered_data)
        print(f"Stream ID: {sensor.stream_id}, Type: {sensor.type}")
        print(f"Processing sensor batch: [{data_label}]")
        print(result)

        print("\nInitializing Transaction Stream...")
        transaction = TransactionStream("TRANS_001")
        transaction_data = ["buy:100", "sell:150", "buy:75"]
        data_label = ""
        i = 0
        for data in transaction_data:
            data_label += data
            i += 1
            if i < len(transaction_data):
                data_label += ", "
        result = transaction.process_batch(transaction_data)
        print(f"Stream ID: {transaction.stream_id}, Type: {transaction.type}")
        print(f"Processing transaction batch: [{data_label}]")
        print(result)

        print("\nInitializing Event Stream...")
        event = EventStream("EVENT_001")
        event_data = ["login", "error", "logout"]
        data_label = ""
        i = 0
        for data in event_data:
            data_label += data
            i += 1
            if i < len(event_data):
                data_label += ", "
        result = event.process_batch(event_data)
        print(f"Stream ID: {event.stream_id}, Type: {event.type}")
        print(f"Processing event batch: [{data_label}]")
        print(result)

    except ValueError as error:
        print(f"Error: {error}")

    print("\n=== Polymorphic Stream Processing ===")

    try:
        streams = [SensorStream("SENSOR_002"),
                   TransactionStream("TRANS_002"),
                   EventStream("EVENT_002")]
        data_batches = [["temp:120,2", "temp:-42", "pressure:2048"],
                        ["buy:696", "sell:-200"],
                        ["login", "error", "logout"]]
        processor = StreamProcessor()
        for stream in streams:
            processor.add_stream(stream)
        processor.run_all(data_batches)
        print("Processing mixed stream types through unified interface.\n")

    except ValueError as error:
        print(f"Error: {error}")

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
