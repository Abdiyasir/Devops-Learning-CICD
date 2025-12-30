resource "aws_instance" "CICD" {
  ami = var.instance_ami
  instance_type = var.instance_type
  vpc_security_group_ids = [aws_security_group.CICD.id]
  key_name = aws_key_pair.deploy.key_name
}



