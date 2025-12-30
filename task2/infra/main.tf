module "ec2" {
  source = "./modules/ec2"
  instance_type = var.instance_type
  instance_ami = var.instance_ami
  key_name = var.key_name
  public_key = var.public_key
}