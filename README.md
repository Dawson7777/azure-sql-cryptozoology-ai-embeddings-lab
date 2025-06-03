# Build 2025 Azure SQL Cryptozoology AI Embeddings Lab

## **Welcome to the Cryptid Research Initiative**

<p align="center">
<img height="200" src="./media/logo3.png" alt="Centered Image">
</p>

Welcome, Investigator, to the **Cryptid Research Initiative**-a clandestine alliance of experts, explorers, and analysts dedicated to uncovering the world's most elusive beings. As a new member, you are now part of a centuries-old tradition of secret scientific inquiry, where we pursue the truth behind the legends that most dismiss as folklore. Our organization has established a global network of field operatives, local informants, and advanced data analysts, all tasked with researching, cataloging, and monitoring cryptid activity around the world. From the misty forests of the Pacific Northwest to the frozen peaks of the Himalayas, and the shadowed billabongs of the Australian outback, our research spans every continent and culture. You will be granted access to confidential video archives, eyewitness accounts, and analytical data-some gathered at great personal risk-so that you may contribute to the ever-growing body of knowledge. 

**Your pivotal role is to harness advanced artificial intelligence tools to analyze rare video evidence and, together with your colleagues, assemble the most comprehensive database of cryptid encounters ever known.** By applying cutting-edge techniques, your work will help reveal patterns, verify authenticity, and propel our understanding further than ever before. 

Welcome to the front lines of cryptozoological discovery-remember, secrecy and scientific rigor are the cornerstones of our society.

**Lab Guide for Azure SQL is [here](./labGuide.md).**

**Lab Guide for SQL Server 2025 is [here](./labGuide_SQL25.md).**

## Prerequisites

- Azure SQL Server and Azure SQL Database (Free offering will work well)
    - Database named "SampleDB" with the Adventureworks sample data loaded
- Azure blob storage
- Azure key vault
- Azure OpenAI
    - gpt-4o
    - text-embedding-ada-002
- Azure AI Foundry hub
- Azure AI Foundry project
- VS Code with the MSSQL Extension
- [MSSQL Python Driver](https://github.com/microsoft/mssql-python)
- Install python libraries via the requirements.txt file
- Place the yeti.mp4 video in an Azure Blob Storage container and generate a SAS URL

## Key Learning Objectives

- Understand new AI features in the SQL database
- Create embeddings with relational data
- Assess similarity searching vs text only
- Design an AI application with relational data
- Implement database security best practices

## Lab Outline

- Connecting to your free Azure SQL Database
- Getting started with REST in the database and Azure AI Content Understanding
- Creating embeddings for relational data with Azure OpenAI
- Create a chat app on your data using RAG and Azure SQL
- Securing your data
- Ledger tables and chat history

## Repository Contents

- lab_files: Contains the files for running the ChainLit app
- media: The image files for the labGuide
- labGuide.md: The workshop guide for Azure SQL
- labGuide_SQL25.md: The workshop guide for SQL Server 2025
- yeti.mp4: The video to be analyzed