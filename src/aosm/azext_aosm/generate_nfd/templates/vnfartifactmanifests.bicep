// Copyright (c) Microsoft Corporation.

// This file creates an NF definition for a VNF
param location string = resourceGroup().location
@description('Name of an existing publisher, expected to be in the resource group where you deploy the template')
param publisherName string 
@description('Name of an existing ACR-backed Artifact Store, deployed under the publisher.')
param acrArtifactStoreName string
@description('Name of an existing Storage Account-backed Artifact Store, deployed under the publisher.')
param saArtifactStoreName string
@description('Name of the manifest to deploy for the ACR-backed Artifact Store')
param acrManifestName string
@description('Name of the manifest to deploy for the Storage Account-backed Artifact Store')
param saManifestName string
@description('The name under which to store the VHD')
param vhdName string
@description('The version that you want to name the NFM VHD artifact, in format A-B-C. e.g. 6-13-0')
param vhdVersion string
@description('The name under which to store the ARM template')
param armTemplateName string
@description('The version that you want to name the NFM template artifact, in format A.B.C. e.g. 6.13.0. If testing for development, you can use any numbers you like.')
param armTemplateVersion string

// Created by the az aosm definition publish command before the template is deployed
resource publisher 'Microsoft.HybridNetwork/publishers@2022-09-01-preview' existing = {
  name: publisherName
  scope: resourceGroup()
}

// Created by the az aosm definition publish command before the template is deployed
resource acrArtifactStore 'Microsoft.HybridNetwork/publishers/artifactStores@2022-09-01-preview' existing = {
  parent: publisher
  name: acrArtifactStoreName
}

// Created by the az aosm definition publish command before the template is deployed
resource saArtifactStore 'Microsoft.HybridNetwork/publishers/artifactStores@2022-09-01-preview' existing = {
  parent: publisher
  name: saArtifactStoreName
}

resource saArtifactManifest 'Microsoft.Hybridnetwork/publishers/artifactStores/artifactManifests@2022-09-01-preview' = {
  parent: saArtifactStore
  name: saManifestName
  location: location
  properties: {
    artifacts: [
      {
        artifactName: '${vhdName}'
        artifactType: 'VhdImageFile'
        artifactVersion: vhdVersion
      }
    ]
  }
}

resource acrArtifactManifest 'Microsoft.Hybridnetwork/publishers/artifactStores/artifactManifests@2022-09-01-preview' = {
  parent: acrArtifactStore
  name: acrManifestName
  location: location
  properties: {
    artifacts: [
      {
        artifactName: '${armTemplateName}'
        artifactType: 'ArmTemplate'
        artifactVersion: armTemplateVersion
      }
    ]
  }
}