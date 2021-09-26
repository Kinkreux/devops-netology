# devops-netology
## Какие файлы будут проигнорированы благодаря ./terraform/.gitignore
**Local .terraform directories**

**/.terraform/* - файлы, находящиеся в директории /.terraform/ или в её поддиректориях рекурсивно, которая будет дочерней директории /terraform/

**.tfstate files**

*.tfstate - файлы, в конце названия которых есть .tfstate рекурсивно (видимо, это расширение)

*.tfstate.* - файлы, в начале или в конце названия которых есть .tfstate рекурсивно (по идее, второе правило включает в себя первое, непонятна разница)

**Crash log files**

crash.log - файлы с названием конкретным названием и расширением crash.log рекурсивно

**Exclude all .tfvars files, which are likely to contain sentitive data, such as password, private keys, and other secrets. These should not be part of version control as they are data points which are potentially sensitive and subject to change depending on the environment.**

*.tfvars - все файлы с конкретным расширением .tfvars рекурсивно

**Ignore override files as they are usually used to override resources locally and so are not checked in**

override.tf - файлы с названием конкретным названием и расширением рекурсивно

override.tf.json - файлы с названием конкретным названием и расширением рекурсивно

*_override.tf файлы - с названием конкретным названием и расширением рекурсивно

*_override.tf.json - файлы с названием конкретным названием и расширением рекурсивно

**Include override files you do wish to add to version control using negated pattern**

!example_override.tf - это правило, с помощью которого можно исключить из игнорирования файлы, заканчивающиеся на override.tf

**Include tfplan files to ignore the plan output of command: terraform plan -out=tfplan**

example: *tfplan* - пример, с помощью которого можно игнорировать файлы, включающие в название tfplan

**Ignore CLI configuration files**

.terraformrc - файлы с конкретным названием

terraform.rc - файлы с конкретным названием и расширениемnew line
new line
