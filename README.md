# S3 Compatible Backup Integration for Home Assistant

Home Assistant integration for enabling backups to any S3-compatible storage provider.

> [!NOTE]
> This is an unofficial integration. It is a lightly modified fork of Home Assistant's core S3 integration with the primary change being the removal of the AWS-only domain restriction for endpoint URLs. This allows users to attempt backups to any S3-compatible service at their own risk, rather than being limited to AWS S3 by the core integration. Use with non-AWS providers is at your own risk regarding compatibility.

## Prerequisites

1. **An S3-Compatible Storage Account & Bucket:**
    * You need an account with an S3-compatible storage provider
    * You must have an existing bucket created on this provider
    * You will need the following credentials:
        * **Access Key ID**
        * **Secret Access Key**
        * **Endpoint URL** for the S3 API
        * **Bucket Name**

## Installation

This integration can be installed via [HACS](https://hacs.xyz/) (Home Assistant Community Store).

1. **Ensure HACS is installed.**
    * You can find installation instructions [here](https://hacs.xyz/docs/use/download/download/).
2. **Add as a Custom Repository**:
    * In Home Assistant, navigate to HACS in your sidebar.
    * Click the three dots in the top right, select "Custom repositories".
    * **Repository:** <https://github.com/pransktr/hassio-s3-compatible>
    * **Type:** Select "Integration".
    * Click "ADD".
3. **Install from HACS:**
    * Search for "S3 Compatible" or "S3 Compatible Backup" in HACS.
    * Click "DOWNLOAD".
    * Restart Home Assistant when prompted.

## Configuration

1. Go to **Settings > Devices & Services** in Home Assistant.
2. Click **"+ ADD INTEGRATION"**.
3. Search for and select **"S3 Compatible"**.
4. A dialog will appear asking for your S3 compatible storage details:
    * **Access Key ID:** Enter the Access Key ID for your S3 provider.
    * **Secret Access Key:** Enter the Secret Access Key for your S3 provider.
    * **Bucket Name:** Enter the name of your existing S3 bucket.
    * **Endpoint URL:** Enter the full S3 API endpoint URL provided by your storage provider (e.g. `https://s3.example.com`).
    * Click **"Submit"**.
5. If the details are correct and Home Assistant can connect to your S3 provider and bucket, the integration will be set up.

## Functionality

This integration acts as a **backup platform** for Home Assistant's built-in backup manager. Once configured, your S3-compatible storage will become an available location for Home Assistant to store its backups.

* **Storage for Core Backups:** Enables Home Assistant's manual ("Create Backup") and automated backup features to use your S3-compatible bucket as a remote storage target.
* **Backup Management:** Allows Home Assistant to list, download, and delete backups stored in this S3-compatible location directly from the Home Assistant UI (**Settings > System > Backups**).

This integration itself does not schedule or create backups; it provides the interface for Home Assistant's core backup system to interact with your S3-compatible storage.
