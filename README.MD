
# Expert.ai Bot Use Case  
Automated administration and generation of clinical summary for in-patient cases by intelligently suggesting ICD10 CM diagnosis codes and extracting associated verbiage (using custom NLP model built with Expert.ai Discovery API), from unstructured medical records while seamlessly handing off to nurse for final assessment in order to perform upstream and downstream processes and validations.

## Prerequisites

- [x] Install **[UiPath Studio - Community Edition](https://download.uipath.com/UiPathStudioSetup.exe)**

## How To's

### Getting and Running the Demo Workflow (Expert.ai Health -  Coder Bot)

1. Download the packaged workflow (.nupkg) [**HERE**](https://github.com/zell12/Expert.ai-Health---Coder-Bot/tree/master/_package).

2. Copy the package (.nupkg) and paste it into `C:\ProgramData\UiPath\Packages`.

3. Open UiPath Assistant, highlight Expert.ai process. Click ![enter image description here](https://i.imgur.com/nokp2La.png) and click Install.

4. Click ![enter image description here](https://i.imgur.com/rdhdSQZ.png) to run the process.

![enter image description here](https://i.imgur.com/E6ghVwT.png)

### Using the Expert system Integrations (to build custom intelligent automation process flows)  

1. Click Manage Packages > All Packages. Search for 'ExpertSystem'. Click Install and Save.

2. Drag and drop the desired activity into the canvas.

		Annotate CogX
			-   Annotates a specified CogX input. A CogX input is a proprietary ExpertSystem XML format
		Annotate File
			-   Annotates a specified file input
		Annotate Text
			-   Annotates a specified text input

3. Supply the necessary parameters.

	    Credentials: Password, ServiceEndpoint, UserName
	    Input: AnnotationPlan, Input [CogX|File|Text], ResponseType [XML|JSON]

![enter image description here](https://i.imgur.com/H10QicZ.gif)

# License  
Copyright (c) Russel Alfeche. All rights reserved.

This project is licensed under the MIT License - see the [LICENSE.MD](LICENSE.MD) file for details