# BlockTrack: Blockchain-Based Supply Chain & Anti-Counterfeiting DApp
**Experiment 10: Blockchain-based Mini Project (Capstone)**

[![Solidity](https://img.shields.io/badge/Solidity-^0.8.20-blue.svg)](https://soliditylang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 1. Project Overview & Real-World Domain
Counterfeiting costs global industries over **$500 Billion** annually, posing severe risks in pharmaceuticals, luxury goods, and electronics. Traditional supply chain systems rely on centralized databases vulnerable to single-point-of-failure, unauthorized data tampering, and lack of end-to-end transparency.

**BlockTrack** is an enterprise-grade Decentralized Application (DApp) that leverages Ethereum blockchain smart contracts to establish an **immutable custody trail** from product manufacturing to consumer delivery.

### Key Capabilities:
- **Role-Based Minting**: Only authorized manufacturers can register and mint genuine products with verified serial numbers.
- **Verifiable Custody Handover**: Only the verified current owner can transfer custody to distributors, retailers, or consumers.
- **Immutable Checkpoints**: Cryptographically logged status milestones (e.g., cold-chain verification, customs clearance).
- **Public Provenance Stepper**: Any consumer or auditor can query a product ID to view its complete authentic timeline.
- **Event-Driven Architecture**: Emits real-time EVM events (`ProductCreated`, `ProductOwnershipTransferred`, `ProductStatusUpdated`).

---

## 2. Project Directory Structure

```text
Blockchain_Capstone_Project/
├── contracts/
│   ├── SupplyChain.sol        # Main Solidity Smart Contract
│   └── SupplyChainTest.sol    # Solidity Unit Tests (for Remix IDE)
├── frontend/
│   ├── index.html             # Responsive Web3 UI
│   ├── style.css              # Dark Glassmorphism Styling
│   ├── app.js                 # Web3 Frontend Logic (Ethers.js v6)
│   └── contractConfig.js      # ABI and Deployed Contract Address
├── scripts/
│   └── deploy.js              # Hardhat / Ethers Deployment Script
├── test/
│   └── supplyChain.test.js    # Hardhat / Chai Unit Test Suite
├── hardhat.config.js          # Hardhat Configuration
├── package.json               # NPM Dependencies & Scripts
├── PROJECT_REPORT.md          # Comprehensive Academic Capstone Project Report
└── README.md                  # Execution & Setup Instructions
```

---

## 3. Quick Run Guide (Method 1: Remix IDE + Browser - Recommended & Zero Setup)

You can run and demonstrate the entire project immediately without installing local Node.js packages!

### Step 1: Open Smart Contract in Remix
1. Open your browser and navigate to [https://remix.ethereum.org](https://remix.ethereum.org).
2. In the File Explorer tab, create a new file named `SupplyChain.sol`.
3. Copy and paste the contents of `contracts/SupplyChain.sol` into Remix.
4. Go to the **Solidity Compiler** tab (left sidebar icon with the compiler logo):
   - Select compiler version `0.8.20` or higher.
   - Click **Compile SupplyChain.sol**.

### Step 2: Deploy Contract
1. Go to the **Deploy & Run Transactions** tab:
   - **Environment**: Select `Remix VM (Cancun)` or `Injected Provider - MetaMask` (if you want to test on Sepolia Testnet).
   - Under Contract, select `SupplyChain - SupplyChain.sol`.
   - Click **Deploy**.
2. Once deployed, expand the contract under **Deployed Contracts** at the bottom left.
3. Click the copy icon next to the deployed contract address (e.g. `0xd9145CCE52D386f254917e481eB44e9943F39138`).

### Step 3: Run the Frontend UI
1. Navigate to the `frontend/` folder on your computer:
   `c:\Users\komal\AndroidStudioProjects\BillingSystem\Blockchain_Capstone_Project\frontend\`
2. Double-click `index.html` to open it in Chrome, Edge, or Firefox.
3. Click **Connect MetaMask** in the top navigation.
4. In the **Contract Address** input box on the web page:
   - Paste the contract address you copied from Remix (or your testnet deployment).
   - Click **Save Address**.
5. You are now fully connected to the blockchain!

---

## 4. Run Guide (Method 2: Hardhat Local Environment)

If you have Node.js installed on your system:

### 1. Install Dependencies
```bash
npm install
```

### 2. Compile Contracts
```bash
npm run compile
```

### 3. Run Automated Unit Tests
```bash
npm run test
```
All 6 test cases testing initialization, product creation, unauthorized access protection, ownership transfer, and history tracking will pass.

### 4. Deploy Locally
In terminal 1:
```bash
npx hardhat node
```
In terminal 2:
```bash
npm run deploy:local
```
This automatically updates `frontend/contractConfig.js` with the fresh deployed contract address!

---

## 5. Walkthrough of Real-World Test Scenario

### Scenario: High-Value Pharmaceutical Vaccine Tracking

| Step | Actor | Action | Expected Output |
| :--- | :--- | :--- | :--- |
| **1. Minting** | Manufacturer | Enter Name: `Pfizer COVID-19 Vaccine Batch 402`<br>Serial: `VAX-2026-991A`<br>Click **Mint & Register Product** | Transaction confirmed. Total products becomes `1`. Status initialized to `Manufactured and Packaged at Facility`. |
| **2. Transit** | Manufacturer | Product ID: `1`<br>New Owner: Distributor Address (`0x70997970C51812dc3A010C7d01b50e0d17dc79C8`)<br>Stage: `In Transit`<br>Notes: `Dispatched via Ultra-Cold Storage Cargo Flight #712`<br>Click **Transfer Custody** | Ownership updates on chain. Stage changes to `In Transit`. |
| **3. Checkpoint**| Distributor | Product ID: `1`<br>Milestone: `Arrived at Regional Distribution Hub. Temperature logged: -70°C`<br>Click **Log Status Checkpoint** | Checkpoint permanently written to blockchain history. |
| **4. Retailer** | Distributor | Product ID: `1`<br>New Owner: Retail Pharmacy Address (`0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC`)<br>Stage: `With Retailer`<br>Notes: `Delivered to Apex Central Pharmacy Hub` | Product is now in possession of the Retailer. |
| **5. Patient Verification** | End Consumer | Go to **Verify Authenticity & Inspect Provenance Trail**.<br>Enter Product ID `1`<br>Click **Track Product** | A complete interactive visual timeline displays all custody handovers, timestamps, checkpoints, and a green badge: **"✔ Genuine & Verified"**. |
