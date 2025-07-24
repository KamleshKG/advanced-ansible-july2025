FROM ubuntu:24.04
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org>

# Install necessary packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openssh-server python3 sudo && \
    apt-get clean

# Setup SSH
RUN mkdir -p /var/run/sshd && \
    echo 'root:root' | chpasswd && \
    sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#\?PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

# Setup root .ssh folder
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh

# SSH Port (default 22) and web (optional)
EXPOSE 22
EXPOSE 80

# Default command: Run SSH daemon in foreground
CMD ["/usr/sbin/sshd", "-D"]
