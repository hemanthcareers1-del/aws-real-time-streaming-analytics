provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "raw_bucket" {
  bucket = "aws-streaming-raw-zone"
}

resource "aws_s3_bucket" "curated_bucket" {
  bucket = "aws-streaming-curated-zone"
}
