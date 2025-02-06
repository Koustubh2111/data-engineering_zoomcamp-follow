variable "project" {
    description = "Project name"
    default =  "terraform-starter-450115"
  
}

variable "region" {
    description = "Region"
    default = "us-east1"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "Name of dataset in bigquery"
  default     = "starter_dataset"
}

variable "gcs_bucket_name" {
  description = "name of the GCS storage bucket"
  default     = "terraform-starter-450115-starter-bucket"

}