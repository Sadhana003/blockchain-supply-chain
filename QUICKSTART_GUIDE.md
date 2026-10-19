# BlockTrack Supply Chain DApp - Quickstart & Execution Guide

Welcome to the **Blockchain-Based Supply Chain & Anti-Counterfeiting DApp**!

---

## 🚀 How to Run the Project (3 Easy Options)

### Option 1: 1-Click Launch (Easiest)
1. Open your desktop folder: `blockchain-supply-chain`
2. **Double-click `start_dapp.bat`**
3. It will automatically start the server and open the DApp in your web browser at `http://localhost:8000`!

### Option 2: Direct Browser Launch
1. Double-click `index.html` to open it in Chrome, Edge, or Brave.

---

## 🧪 Instant Simulator Mode (No MetaMask or Gas Needed)

If you don't have MetaMask installed yet or just want to test all features immediately:
1. Open the DApp in your browser.
2. Click **"🧪 Switch to Instant Simulator Mode"** at the top.
3. You can now test:
   - **Minting products** with unique serial numbers.
   - **Logging milestone checkpoints** (Cold storage, customs, quality inspections).
   - **Transferring custody** across the 4 stages (In Transit, Distributor, Retailer, Consumer).
   - **Tracking provenance** with the full interactive visual timeline!

---

## 🌐 Web3 Blockchain Mode (Connecting to Real Ethereum / Sepolia)

### Step 1: Open & Compile Smart Contract
1. Go to **[https://remix.ethereum.org](https://remix.ethereum.org)**.
2. In the File Explorer tab, create a new file: `SupplyChain.sol`.
3. Copy all the code from `contracts/SupplyChain.sol` into Remix.
4. Click the **Solidity Compiler** tab on the left (the 'S' logo).
5. Select compiler `0.8.20` and click **Compile SupplyChain.sol** (green checkmark appears).

### Step 2: Deploy Contract
1. Click the **Deploy & Run Transactions** tab (Ethereum logo with arrow).
2. Set **Environment**:
   - For fast in-browser testing: `Remix VM (Cancun)`
   - For MetaMask on Sepolia testnet: `Injected Provider - MetaMask`
3. Click the orange **Deploy** button.
4. Under **Deployed Contracts** at the bottom left, copy the deployed contract address (e.g. `0xd9145CCE52D386f254917e481eB44e9943F39138`).

### Step 3: Connect DApp to Contract
1. In your DApp browser window, click **Connect MetaMask**.
2. Paste the contract address into the **Contract Address** input bar.
3. Click **Save Address**.

---

## 📋 Full Supply Chain Testing Scenario

| Step | Action | Form to Use | Inputs | Expected Result |
| :---: | :---: | :---: | :---: | :---: |
| **1** | **Mint Product** | 🏭 Register Product | Name: `Pfizer Vaccine Vial`<br>Serial: `LOT-2026-X4` | Product #1 is permanently recorded. Initial status: *Manufactured and Packaged at Facility*. |
| **2** | **Update Status** | 📝 Milestone Checkpoint | Product ID: `1`<br>Milestone: `Passed Ultra-Cold Storage Quality Check (-70°C)` | Milestone is permanently added to the history timeline. |
| **3** | **Custody Handover** | 🔄 Transfer Custody | Product ID: `1`<br>Recipient: *(Distributor address)*<br>Stage: `1: In Transit`<br>Notes: `Dispatched via Temperature-Controlled Air Cargo #410` | Ownership is transferred to Distributor. |
| **4** | **Retail Delivery** | 🔄 Transfer Custody | Product ID: `1`<br>Recipient: *(Retail pharmacy address)*<br>Stage: `3: With Retailer`<br>Notes: `Received at Apex Pharmacy Vault` | Ownership is transferred to Retailer. |
| **5** | **Verify Provenance** | 🔍 Verify Authenticity | Product ID: `1`<br>Click **Track Product** | Renders full timeline with timestamps, addresses, and green badge: **"✔ Genuine & Verified"**. |

---

## 🛠️ Diagnostics & Verification
To verify the entire smart contract logic offline, run in PowerShell:
```powershell
python test_all.py
```
Expected output:
```text
[PASS] 1. Smart Contract file exists and contains all required core functions.
[PASS] 2. Full supply chain lifecycle simulation and access controls verified successfully.
ALL TESTS PASSED! LOGIC & FLOW ARE 100% SOUND.
```
