variable "instance_type" {
  type        = string
  description = "EC2 instance type for task2"
}

variable "instance_ami" {
  type        = string
  description = "ami ID for for task2"
}
variable "key_name" {
  type        = string
}

variable "public_key" {
  type        = string
}