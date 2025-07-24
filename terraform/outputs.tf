output "instance_id" {
  description = "The ID of the EC2 instance"
  value       = aws_instance.bpf_detector.id
}

output "public_ip" {
  description = "Public IP address of the instance"
  value       = aws_instance.bpf_detector.public_ip
}
