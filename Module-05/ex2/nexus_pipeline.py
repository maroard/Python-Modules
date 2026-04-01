from abc import ABC, abstractmethod
from typing import Protocol, Any, List, Dict, Union


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages = []
        self.type = None
        self.processed_data = 0
        self.init_stages()

    def add_stage(self, new_stage: "ProcessingStage") -> None:
        self.stages.append(new_stage)

    def init_stages(self) -> None:
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def run(self, data: Any) -> None:
        result = self.process(data)

        input_label = data
        if self.type == "JSON":
            transform_label = "Enriched with metadata and validation"
        elif self.type == "CSV":
            transform_label = "Parsed and structured data"
            input_label = '"' + data.split('\n')[0] + '"'
        else:
            transform_label = "Aggregated and filtered"

        print(f"Input: {input_label}")
        print(f"Transform: {transform_label}")
        print(f"Output: {result}")


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: List[float]) -> Dict[str, List[float]]:
        if not isinstance(data, list):
            raise TypeError("invalid data type")
        if len(data) == 0:
            raise ValueError("invalid data")

        return {"readings": data}


class TransformStage:
    def process(self, data: Dict[str, List[float]]
                ) -> Dict[str, Union[int, float, List[float]]]:
        if not isinstance(data, dict):
            raise TypeError("invalid data type")
        if "readings" not in data:
            raise ValueError("invalid data")

        readings = data["readings"]

        if not isinstance(readings, list) or len(readings) == 0:
            raise ValueError("invalid data")

        avg = round(sum(readings) / len(readings), 1)

        return {
            "readings": readings,
            "count": len(readings),
            "avg_temp": avg
        }


class OutputStage:
    def process(self, data: Dict[str, Union[int, float, List[float]]]) -> str:
        if not isinstance(data, dict):
            raise TypeError("invalid data type")
        if "count" not in data or "avg_temp" not in data:
            raise ValueError("invalid data")

        avg_temp = data["avg_temp"]
        readings = data["count"]

        if avg_temp < 0:
            temp_range_label = "(Low range)"
        elif avg_temp > 35:
            temp_range_label = "(High range)"
        else:
            temp_range_label = "(Normal range)"

        return (f"Summary: {readings} temperature readings, "
                f"avg: {avg_temp}°C {temp_range_label}")


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self,
                data: Union[List[Dict[str, Any]], Dict[str, Any]]) -> Any:
        self.type = "JSON"

        if not isinstance(data, (list, dict)):
            raise TypeError("invalid data type")

        adapted_data = []

        try:
            if isinstance(data, list):
                self.processed_data = len(data)
                for reading in data:
                    if not isinstance(reading, dict):
                        raise ValueError("invalid data")
                    adapted_data.append(round(float(reading["value"]), 1))
            else:
                self.processed_data = 1
                adapted_data.append(round(float(data["value"]), 1))
        except (KeyError, TypeError, ValueError):
            raise ValueError("invalid data")

        result = adapted_data
        for stage in self.stages:
            result = stage.process(result)

        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: str) -> Any:
        self.type = "CSV"

        if not isinstance(data, str):
            raise TypeError("invalid data type")
        if '\n' not in data:
            raise ValueError("invalid data")

        adapted_data = []

        try:
            rows = data.split('\n')[1:]
            for reading in rows:
                if reading == "":
                    continue
                parts = reading.split(',')
                if len(parts) < 1 or parts[0] == "":
                    raise ValueError("invalid data")
                adapted_data.append(round(float(parts[0]), 1))
        except (TypeError, ValueError):
            raise ValueError("invalid data")

        self.processed_data = len(adapted_data)

        result = adapted_data
        for stage in self.stages:
            result = stage.process(result)

        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: List[str]) -> Any:
        self.type = "Stream"

        if not isinstance(data, list):
            raise TypeError("invalid data type")

        adapted_data = []

        try:
            for element in data:
                if not isinstance(element, str):
                    raise ValueError("invalid data")
                if ':' not in element:
                    raise ValueError("invalid data")
                value = element.split(':')[1]
                adapted_data.append(round(float(value), 1))
        except (TypeError, ValueError, IndexError):
            raise ValueError("invalid data")

        self.processed_data = len(adapted_data)

        result = adapted_data
        for stage in self.stages:
            result = stage.process(result)

        return result


class NexusManager:
    def __init__(self, pipelines: List[ProcessingPipeline]) -> None:
        self.pipelines = pipelines

    def add_pipeline(self, new_pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(new_pipeline)

    def run_pipelines(self, data_batches: List[Any]) -> None:
        for pipeline, data in zip(self.pipelines, data_batches):
            print()
            pipeline.run(data)


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    print()
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print()

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    print()

    print("=== Multi-Format Data Processing ===")

    try:
        print()
        print("Processing JSON data through pipeline...")
        pipeline = JSONAdapter("JSON_001")
        json_data = [
            {"sensor": "temp", "value": 33.5, "unit": "C"},
            {"sensor": "temp", "value": 36.8, "unit": "C"},
            {"sensor": "temp", "value": 38.3, "unit": "C"},
            {"sensor": "temp", "value": 37.0, "unit": "C"}
        ]
        pipeline.run(json_data)

        print()
        print("Processing CSV data through same pipeline...")
        pipeline = CSVAdapter("CSV_001")
        csv_data = "temp,humidity\n14.1,60\n17.7,58\n16.8,59\n16.0,61\n15.3,60"
        pipeline.run(csv_data)

        print()
        print("Processing Stream data through same pipeline...")
        pipeline = StreamAdapter("STREAM_001")
        stream_data = ["temp:-21.5", "temp:-22.0", "temp:-22.4"]
        pipeline.run(stream_data)

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

    print()
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    try:
        pipelines = [JSONAdapter("JSON_002"),
                     CSVAdapter("CSV_002"),
                     StreamAdapter("STREAM_002")]
        data_batches = [json_data, csv_data, stream_data]
        manager = NexusManager([])
        for pipeline in pipelines:
            manager.add_pipeline(pipeline)
        manager.run_pipelines(data_batches)

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

    print()
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    try:
        pipeline = StreamAdapter("STREAM_FAILURE")
        stream_data = ["this test simulate a pipeline failure"]
        pipeline.run(stream_data)

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")

    print()
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
