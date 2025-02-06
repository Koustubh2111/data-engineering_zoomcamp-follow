terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.19.0"
    }
  }
}

provider "google" {
  project     = "terraform-starter-xxxxx"
  region      = "us-east1"
}

resource "google_storage_bucket" "starter-bucket" {
  name          = "terraform-starter-xxxxx-starter-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}