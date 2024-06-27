import subprocess
from pipeline import Pipelinee
import argparse
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start data ingestion pipeline or UI.")
    parser.add_argument("--data_ingest", action="store_true", help="Start data ingestion pipeline")
    parser.add_argument("--chat", action="store_true", help="Start chat UI")
    args = parser.parse_args()
 
    if args.data_ingest:
        # If --ingest argument provided, run the data ingestion pipeline
        pipeline_instance = Pipelinee()
        pipeline_instance.run_pipelinee()
       
    elif args.chat:
        # If --chat argument provided, start the UI using chainlit
        subprocess.run(["chainlit", "run", "app.py", "-w"])
    else:
        # If no argument provided or unrecognized argument, display usage information
        parser.print_help()
 