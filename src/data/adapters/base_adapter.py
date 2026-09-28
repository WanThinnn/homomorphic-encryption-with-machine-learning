from abc import ABC, abstractmethod

class BaseAdapter(ABC):
    """
    Base interface for all Data Adapters.
    Production UEBA systems use this to ingest logs from various sources
    (CERT, Elastic ECS, Splunk CIM, AWS OCSF) and convert them to 
    a standardized 17-dimensional behavioral feature vector.
    """

    @abstractmethod
    def extract_features(self, raw_dir: str, output_dir: str) -> str:
        """
        Parse raw logs from the source and save the standardized features 
        to output_dir / behavioral_features.csv.

        Returns:
            str: Path to the generated CSV file.
        """
        pass
