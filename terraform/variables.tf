variable "aws_access_key" {
  description = "Your AWS Access Key"
  type        = string
  sensitive   = true
}

variable "aws_secret_key" {
  description = "Your AWS Secret Access Key"
  type        = string
  sensitive   = true
}

variable "key_name" {
  description = "Name of the AWS Key Pair to use"
  type        = string
}
