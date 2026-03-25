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
            if not isinstance(element, str):
                raise ValueError("invalid data")
            if criteria in element:
                filtered_batch.append(element)
        return filtered_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.type,
            "processed_data": self.processed_data
        }

    def run(self, data_batch):
        data_label = ""
        i = 0
        for data in data_batch:
            data_label += data
            i += 1
            if i < len(data_batch):
                data_label += ", "

        result = self.process_batch(data_batch)
        if "Environmental" in self.type:
            type_label = "sensor"
        elif "Financial" in self.type:
            type_label = "transaction"
        else:
            type_label = "event"

        print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        print(f"Processing {type_label} batch: [{data_label}]")
        print(result)
        print()


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.extreme_temp = 0
        self.avg_temp = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.type = "Environmental Data"
        self.processed_data = len(data_batch)

        values = []
        filtered_batch = self.filter_data(data_batch, "temp:")
        try:
            for element in filtered_batch:
                values.append(float(element.split(':')[1]))
        except ValueError:
            raise ValueError("invalid data")

        self.extreme_temp = 0
        self.avg_temp = 0
        total_temp = 0
        if len(values) > 0:
            for value in values:
                if value >= 100 or value <= -20:
                    self.extreme_temp += 1
                total_temp += value
            self.avg_temp = total_temp / len(values)

        readings_label = "reading" if self.processed_data <= 1 else "readings"

        return ("Sensor analysis: "
                f"{self.processed_data} {readings_label} processed, "
                f"avg temp: {self.avg_temp}°C")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["avg_temp"] = self.avg_temp
        stats["extreme_temp"] = self.extreme_temp
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.net_flow = 0
        self.large_trans = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.type = "Financial Data"
        self.processed_data = len(data_batch)

        values = []
        try:
            for element in data_batch:
                action, value = element.split(':')
                if action == "buy":
                    if int(value) < 0:
                        values.append(- int(value))
                    else:
                        values.append(int(value))
                elif action == "sell":
                    if int(value) < 0:
                        values.append(int(value))
                    else:
                        values.append(- int(value))
        except ValueError:
            raise ValueError("invalid data")

        self.net_flow = 0
        self.large_trans = 0
        for value in values:
            self.net_flow += value
            if value >= 500 or value <= -500:
                self.large_trans += 1

        op_label = "operation" if self.processed_data <= 1 else "operations"
        sign = "+" if self.net_flow >= 0 else "-"
        value = abs(self.net_flow)
        units_label = "unit" if self.net_flow in [-1, 0, 1] else "units"

        return (f"Transaction analysis: {self.processed_data} {op_label}, "
                f"net flow: {sign}{value} {units_label}")

    def get_stats(self):
        stats = super().get_stats()
        stats["net_flow"] = self.net_flow
        stats["large_trans"] = self.large_trans
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.errors_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.type = "System Events"
        self.processed_data = len(data_batch)

        for element in data_batch:
            if not isinstance(element, str):
                raise ValueError("invalid data")
            if element not in ["login", "logout", "error"]:
                raise ValueError("unknown event")

        self.errors_count = 0
        for element in data_batch:
            if element == "error":
                self.errors_count += 1

        errors_label = "error" if self.errors_count in [0, 1] else "errors"
        events_label = "event" if self.processed_data <= 1 else "events"

        return (f"Event analysis: {self.processed_data} {events_label}, "
                f"{self.errors_count} {errors_label}")

    def get_stats(self):
        stats = super().get_stats()
        stats["errors_count"] = self.errors_count
        return stats


class StreamProcessor():
    def __init__(self):
        self.streams = []

    def add_stream(self, new_stream):
        self.streams.append(new_stream)

    def run_all(self, data_batches):
        print("Processing mixed stream types through unified interface.\n")

        print("Batches Results:")
        i = 0
        extreme_temp = 0
        large_trans = 0
        errors_count = 0

        for stream in self.streams:
            stream.process_batch(data_batches[i])
            stats = stream.get_stats()

            type = stats["type"]
            processed_data = stats["processed_data"]
            if "Environmental" in type:
                type = "Sensor"
                process_label = ("reading" if processed_data <= 1
                                 else "readings")
                extreme_temp += stats["extreme_temp"]
            elif "Financial" in type:
                type = "Transaction"
                process_label = ("operation" if processed_data <= 1
                                 else "operations")
                large_trans += stats["large_trans"]
            else:
                type = "Event"
                process_label = ("event" if processed_data <= 1
                                 else "events")
                errors_count += stats["errors_count"]
            print(f"- {type} data: {processed_data} {process_label} processed")
            i += 1
        print()

        print("Stream filtering active: High-priority data only")
        alert_label = "alert" if extreme_temp <= 1 else "alerts"
        trans_label = "transaction" if large_trans <= 1 else "transactions"
        errors_label = "error" if errors_count <= 1 else "errors"
        print("Filtered results: "
              f"{extreme_temp} critical sensor {alert_label}, "
              f"{large_trans} large {trans_label}, "
              f"{errors_count} {errors_label} encountered")
        print()


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    try:
        print("Initializing Sensor Stream...")
        stream = SensorStream("SENSOR_001")
        data_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
        stream.run(data_batch)

        print("Initializing Transaction Stream...")
        stream = TransactionStream("TRANS_001")
        data_batch = ["buy:100", "sell:150", "buy:75"]
        stream.run(data_batch)

        print("Initializing Event Stream...")
        stream = EventStream("EVENT_001")
        data_batch = ["login", "error", "logout"]
        stream.run(data_batch)

    except ValueError as error:
        print(f"Error: {error}")
        print()

    print("=== Polymorphic Stream Processing ===")

    try:
        streams = [SensorStream("SENSOR_002"),
                   TransactionStream("TRANS_002"),
                   EventStream("EVENT_002")]
        data_batches = [["temp:120", "temp:-30"],
                        ["buy:100", "sell:150", "buy:600", "sell:25"],
                        ["login", "logout", "error"]]
        processor = StreamProcessor()
        for stream in streams:
            processor.add_stream(stream)
        processor.run_all(data_batches)

    except ValueError as error:
        print(f"Error: {error}")
        print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
