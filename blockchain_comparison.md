
# Blockchain Platform Comparison

## Comparison Table

| Blockchain Name    | Type          | Consensus Mechanism Used    | Permission Model  | Speed / Throughput (TPS) | Smart Contract Support | Token Support   | Typical Use Case                  | Notable Technical Feature         |
|--------------------|---------------|----------------------------|-------------------|-------------------------|------------------------|-----------------|-----------------------------------|-----------------------------------|
| Ethereum           | Public        | Proof of Stake (PoS)       | Open              | ~15–30 TPS               | Yes (Solidity)         | Native (ETH)     | Decentralized applications (DApps) | Large developer ecosystem, EVM    |
| Hyperledger Fabric | Private       | Pluggable (default: Raft)  | Permissioned      | Up to 20,000 TPS (tested) | Yes (Chaincode in Go, Java, Node.js) | No native token  | Enterprise supply chain & business | Modular architecture, pluggable consensus |
| R3 Corda           | Consortium    | Notary-based consensus (varies by network) | Permissioned      | 100–300 TPS (varies)    | Yes (JVM-based, Kotlin/Java) | No native token  | Inter-bank settlement, finance     | Privacy-focused point-to-point transactions |

---

## Short Report

The three blockchain platforms—Ethereum, Hyperledger Fabric, and R3 Corda—offer distinct technical capabilities tailored to different use cases.

**Ethereum**, as a public blockchain, is open and decentralized. It uses Proof of Stake to validate transactions and supports smart contracts via Solidity on the Ethereum Virtual Machine (EVM). Ethereum is ideal for building decentralized applications (DApps) where trustless interaction is key, but its throughput remains relatively modest (~15–30 TPS).

**Hyperledger Fabric** is a private blockchain designed for enterprise applications. Its permissioned model supports fine-grained access control and high performance (up to 20,000 TPS). Fabric offers modular consensus and supports smart contracts in multiple languages, making it suitable for supply chain networks where participants are known.

**R3 Corda** is a consortium blockchain optimized for financial applications among trusted participants. It leverages a unique notary-based consensus model and point-to-point messaging for privacy. It supports smart contracts written in JVM languages and is commonly used in inter-bank financial networks.

### Platform Recommendations:

- For a **decentralized app** → *Ethereum* is preferred due to its public, open model and broad DApp ecosystem.
- For a **supply chain network among known partners** → *Hyperledger Fabric* excels with high throughput, modularity, and permissioned controls.
- For an **inter-bank financial application** → *R3 Corda* is ideal due to its privacy features, legal contract alignment, and support for complex financial workflows.

---
