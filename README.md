### Getting started with AWS CDK
* https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

* Familiarity with AWS CloudFormation is also useful, as **the output of an AWS CDK program is an AWS CloudFormation template**.

* You create **Constructs** inside a **Stack**. Each construct can have one or multiple concrete AWS Resources.

* Construucts and Stacks are represented as classes.

* The AWS CDK includes a library of AWS constructs called the **AWS Construct Library**, organized into various modules. 

* The main CDK package is called `aws-cdk-lib`, and it contains the majority of the AWS Construct Library, along with base classes like `Stack` and `App` used in most CDK applications.

* Install: `python -m pip install aws-cdk-lib`

* Import: `import aws_cdk as cdk`

### Constructs

* Constructs come in three fundamental flavors:
    * **AWS CloudFormation-only or L1**: hese constructs correspond directly to resource types defined by AWS CloudFormation, so when a new AWS service is launched, the AWS CDK supports it a short time after AWS CloudFormation does. AWS CloudFormation resources always have names that begin with `Cfn`. For example, for the Amazon S3 service, `CfnBucket` is the `L1` construct for an Amazon S3 bucket.All L1 resources are in `aws-cdk-lib`.
    * **Curated or L2**: These constructs are carefully developed by the AWS CDK team to address specific use cases and simplify infrastructure development. For the most part, they encapsulate L1 resources, providing sensible defaults and best-practice security policies. For example, `Bucket` is the `L2` construct for an Amazon S3 bucket. `aws-cdk-lib contains L2 constructs that are designated stable`, i.e., ready for production use. If a service's L2 support is still under development, its constructs are designated experimental and provided in a separate module.
    * **Pattern or L3**: Patterns declare multiple resources to create entire AWS architectures for particular use cases. All the plumbing is already hooked up, and configuration is boiled down to a few important parameters. As with L2 constructs, L3 constructs that are ready for production use (stable) are included in aws-cdk-lib

* Finally, the `constructs package` contains the `Construct base class`. It's in its own package because it is used not only by the AWS CDK but also by other construct-based tools, including CDK for Terraform and CDK for Kubernetes.

### Prerequisites

* Need Node.js 10.13.0 or later.

* Configure your credentials using `aws configure`.

* Python 3.6 or later including pip and virtualenv.

### Install the AWS CDK

* `sudo npm install -g aws-cdk`

### Bootstrapping
* Deploying stacks with the AWS CDK requires dedicated Amazon S3 buckets and other containers to be available to AWS CloudFormation during deployment.
* `cdk bootstrap aws://ACCOUNT-NUMBER/REGION`

### Your first AWS CDK app

* Now let's see how it feels to work with the AWS CDK by building the simplest possible AWS CDK app. In this tutorial, you'll learn about the structure of a AWS CDK project, how to use the AWS Construct Library to define AWS resources using code, and how to synthesize, diff, and deploy collections of resources using the AWS CDK Toolkit command-line tool.
    1) Create the app from a template provided by the AWS CDK
    2) Add code to the app to create resources within stacks
    3) Build the app (optional; the AWS CDK Toolkit will do it for you if you forget)
    4) Synthesize one or more stacks in the app to create an AWS CloudFormation template
    5) Deploy one or more stacks to your AWS account
* The build step catches syntax and type errors. The synthesis step catches logical errors in defining your AWS resources. The deployment may find permission issues. As always, you go back to the code, find the problem, fix it, then build, synthesize and deploy again.
* This tutorial walks you through creating and deploying a simple AWS CDK app, from initializing the project to deploying the resulting AWS CloudFormation template. The app contains one stack, which contains one resource: an Amazon S3 bucket.

### Create the App
* Each AWS CDK app should be in its own directory, with its own local module dependencies. Create a new directory for your app. Starting in your home directory, or another directory if you prefer, issue the following commands.
```
mkdir hello-cdk
cd hello-cdk
```
* Now initialize the app using the cdk init command, specifying the desired template ("app") and programming language. That is: `cdk init app --language python`
* After the app has been created, also enter the following two commands to activate the app's Python virtual environment and install the AWS CDK core dependencies:
```
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### List the stacks in the app
* cdk ls

### Add an Amazon S3 bucket
* At this point, your app doesn't do anything because the stack it contains doesn't define any resources. Let's add an Amazon S3 bucket.
* In `hello_cdk/hello_cdk_stack.py`:
```
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
            
class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)
```

### Synthesize an AWS CloudFormation template
* `cdk synth`
* This generates the Cloudformation template on `cdk.out/`

### cdk deploy
* `cdk deploy`
* It is optional (though good practice) to synthesize before deploying. The AWS CDK synthesizes your stack before each deployment.

### Modifying the app
* Update on `hello_cdk/hello_cdk_stack.py`
```
bucket = s3.Bucket(self, "MyFirstBucket",
    versioned=True,
    removal_policy=cdk.RemovalPolicy.DESTROY,
    auto_delete_objects=True)
```
* `cdk diff`

* `cdk deploy`

### Destroying the app's resources

* `cdk destroy`