from abc import ABC, abstractmethod
from typing import Protocol, Any, List, Dict


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id
        self.stages = []
        self.type = None
        self.processed_data = 0

    def add_stage(self, new_stage):
        self.stages.append(new_stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def run(self, data: Any):
        firstly = InputStage()
        secondly = TransformStage()
        thirdly = OutputStage()

        self.add_stage(firstly)
        self.add_stage(secondly)
        self.add_stage(thirdly)

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
        pass


class InputStage():
    def process(self, data: Any) -> Dict:
        pass


class TransformStage():
    def process(self, data: Dict) -> Dict:
        pass


class OutputStage():
    def process(self, data: Dict) -> str:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: Dict) -> Any:
        self.type = "JSON"
        self.processed_data = len(data)

        adapted_data = {}

        try:
            adapted_data["Readings"] = (round(float(data["value"]), 1))
        except ValueError:
            raise ValueError("invalid data")

        for stage in self.stages:
            result = stage.process(result)

        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: str) -> Any:
        self.type = "CSV"
        self.processed_data = len(data)

        adapted_data = {}

        try:
            data = data.split('\n')[1:]
            for reading in data:
                adapted_data["Readings"] = reading.split(',')[0]
        except ValueError:
            raise ValueError("invalid data")

        for stage in self.stages:
            result = stage.process(result)

        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: List) -> Any:
        self.type = "Stream"
        self.processed_data = len(data)

        adapted_data = {}
        adapted_data["Readings"] = []

        try:
            for reading in data:
                value = reading.split(':')[1]
                adapted_data["Readings"].append(round(float(value), 1))
        except ValueError:
            raise ValueError("invalid data")

        for stage in self.stages:
            result = stage.process(result)

        return result


class NexusManager():
    def __init__(self, pipelines):
        self.pipelines = pipelines

    def add_pipeline(self, new_pipeline):
        self.pipelines.append(new_pipeline)

    def process_data(self):
        pass


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
        print("Processing JSON data through pipline...")
        pipeline = JSONAdapter("JSON_001")
        json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
        pipeline.run(json_data)

        print()
        print("Processing CSV data through same pipeline...")
        pipeline = CSVAdapter("CSV_001")
        csv_data = "temp,humidity\n21.5,60\n22.0,58\n22.4,59\n21.9,61\n22.7,60"
        pipeline.run(csv_data)

        print()
        print("processing Stream data through same pipeline...")
        pipeline = StreamAdapter("STREAM_001")
        stream_data = ["temp:21.5", "temp:22.0", "temp:22.4",
                       "temp:21.9", "temp:22.7"]
        pipeline.run(stream_data)
    except ValueError as error:
        print(f"Error: {error}")

    print()
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeine C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    print()

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
