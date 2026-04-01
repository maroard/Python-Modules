from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("invalid data")
        data_sum = sum(data)
        data_average = data_sum / len(data)
        return (f"Processed {len(data)} numeric values, sum={data_sum}"
                f", avg={data_average}")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            return False
        for element in data:
            if not isinstance(element, int):
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("invalid data")
        words_count = len(data.split())
        return f"Processed text: {len(data)} characters, {words_count} words"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or len(data) == 0:
            return False
        return True


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("invalid data")
        log = data.split(':')
        level = log[0].strip()
        message = log[1].strip()
        prefix = "[INFO]" if level == "INFO" else "[ALERT]"
        return f"{prefix} {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or len(data) == 0:
            return False
        log = data.split(":")
        if len(log) != 2:
            return False
        level = log[0].strip()
        message = log[1].strip()
        if (level != "INFO" and level != "ERROR") or len(message) == 0:
            return False
        return True


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    processor = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    try:
        print(f"Processing data: {data}")
        output = processor.format_output(result=processor.process(data))
        print("Validation: Numeric data verified")
        print(output)
    except ValueError as error:
        print(f"Error: {error}")

    print("\nInitializing Text Processor...")
    processor = TextProcessor()
    data = "Hello Nexus World"
    try:
        print(f"Processing data: \"{data}\"")
        output = processor.format_output(result=processor.process(data))
        print("Validation: Text data verified")
        print(output)
    except ValueError as error:
        print(f"Error: {error}")

    print("\nInitializing Log Processor...")
    processor = LogProcessor()
    data = "ERROR: Connection timeout"
    try:
        print(f"Processing data: \"{data}\"")
        output = processor.format_output(result=processor.process(data))
        print("Validation: Log entry verified")
        print(output)
    except ValueError as error:
        print(f"Error: {error}")

    print("\n=== Polymorphic Processing Demo ===\n")
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data = [[1, 2, 3], "Banana Prime", "INFO: System ready"]
    try:
        print("Processing multiple data types through same interface...")
        for i in range(len(data)):
            result = processors[i].process(data[i])
            print(f"Result {i + 1}: {result}")
        print("\nFoundation systems online. Nexus ready for advanced streams.")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
