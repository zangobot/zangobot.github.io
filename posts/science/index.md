---
layout: default
title: Science Publications
---
# Publications by year

<div style="margin-bottom:1rem;">
  <input type="text" id="pub-search" placeholder="Search publications...">
</div>
<script>
document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('pub-search');
  function build() {
    const links = document.querySelectorAll('strong a');
    links.forEach(link => {
      const strong = link.closest('strong');
      if (!strong) return;
      const paragraph = strong.parentNode; // <p>
      if (paragraph.classList.contains('publication')) return;

      const wrapper = document.createElement('div');
      wrapper.className = 'publication';

      // Find the <br> that separates this publication from the next
      let end = paragraph.nextElementSibling;
      while (end && end.tagName !== 'BR') {
        end = end.nextElementSibling;
      }

      // Move all nodes from paragraph up to (but not including) the <br> into wrapper
      const grandParent = paragraph.parentNode;
      grandParent.insertBefore(wrapper, paragraph);
      let node = paragraph;
      while (node && node !== end) {
        const next = node.nextSibling; // include text nodes
        wrapper.appendChild(node);
        node = next;
      }

      // Store searchable text (title, authors, venue)
      wrapper.dataset.text = link.textContent.toLowerCase();
    });
  }

  build();

  input.addEventListener('input', () => {
    const q = input.value.toLowerCase().trim();
    document.querySelectorAll('.publication').forEach(pub => {
      pub.style.display = pub.dataset.text.includes(q) ? '' : 'none';
    });
  });
});
</script>

## 2026
**[Windows Malware Detector as a Compound AI System: Trade-Offs in Accuracy, Efficiency, and Adversarial Robustness](https://arxiv.org/abs/2609.08394)**
  *Authors:* Andrea Ponte, Luca Demetrio, Luca Oneto, Battista Biggio, Fabio Roli
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

Industrial Windows malware detectors are commonly described as Compound AI Systems composed of multiple heterogeneous components, including rule-based mechanisms as well as machine-learning-based static and dynamic analyses. However, due to industrial secrecy and limited public disclosure, the internal architectures of these systems can only be inferred, rendering systematic evaluations of detection accuracy, computational costs, and adversarial robustness largely infeasible. In contrast, academic research provides reproducible and transparent evaluation methodologies, but typically investigates individual detection components in isolation. To bridge the gap between academic research and industrial practice, and inspired by state-of-the-art industrial architectures for Windows malware detection, we propose a novel methodology that (i) explicitly balances the trade-off among detection performance, computational requirements, and robustness, and introduces (ii) system-level threat models that capture how attackers exploit different degrees of knowledge to evade the entire Compound AI System rather than isolated detectors. Experiments conducted on real-world data demonstrate that the Compound AI System training time can be reduced and responsiveness improved while incurring only a marginal loss in detection performance. Leveraging our threat modeling, we show that increasingly knowledgeable attackers craft more effective adversarial examples, revealing the system's strengths and weaknesses, degrading its responsiveness, and exposing a direct trade-off between efficiency and robustness. Finally, we translate these trade-offs into take-home messages and deployment guidelines, helping practitioners to select the system that best matches their operational constraints.

  </details>
<br>
**[EXE-Bench: Ranking the Tradeoffs of AI-based Windows Malware Detectors for Real-World Usability](https://arxiv.org/abs/2607.24177)**
  *Authors:* Andrea Ponte, Daniel Gibert, Matouš Kozák, Dmitrijs Trizna, Maura Pintor, Battista Biggio, Fabio Roli, Luca Demetrio
  *Published on:* IEEE Transactions on Information Forensics and Security
  <details>
    <summary>Abstract</summary>

Due to the lack of systematic evaluations, we are not yet able to determine which AI-based Windows malware detector to deploy in production, since existing evaluations (i) differ in terms of data used for both training and testing; (ii) do not consider temporal analysis to showcase whether models withstand the passage of time; (iii) avoid security evaluations with adversarial attacks that could highlight their brittleness against content-injection attacks; and (iv) neglect the computational requirements for deployment, risking slow inference on endpoints. For these reasons, we develop EXE-Bench, a comprehensive benchmark of AI-based Windows malware detectors. EXE-Bench assesses performance, temporal and adversarial robustness, and computational overhead, aggregating them into a single score for direct and fair model comparison. Through EXE-Bench, we highlight how evaluations conducted only after deployment are suboptimal and unable to provide a complete picture of their performance. In particular, through our analysis, we remark how much domain knowledge instilled through feature engineering is still extremely useful in this domain, resisting both time and adversarial attacks, in stark contrast with most of the deep networks that only excel right after deployment.

  </details>
<br>
**[DroidBreaker: Practical and Functional Problem-Space Attacks on Machine-Learning Android Malware Detectors](https://arxiv.org/abs/2606.26707)**
  *Authors:* Christian Scano, Diego Soi, Angelo Sotgiu, Luca Demetrio, Davide Maiorca, Giorgio Giacinto, Fabio Roli, Battista Biggio
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

Adversarial APKs are Android applications modified in the problem space to evade machine-learning malware detectors. In this work, we first show that, despite claims, existing problem-space attacks remain largely impractical. Most techniques leverage software transplantation to inject entire benign modules, introducing many side-effect features and often causing build-time failures. Fine-grained methods that inject only a narrow subset of components exhibit limited effectiveness, while those that also use obfuscation rely on brittle bytecode rewriting, producing APKs that are syntactically valid but semantically unusable. Prior work further overestimates attack success rates by running smoke tests that only validate installation and basic execution, without assessing whether the modified APK still preserves its intended behavior. To overcome these limitations, we present DROIDBREAKER, a practical (build-safe) and functional (semantics-preserving) problem-space attack framework that provides: (i) query-efficient white- and black-box attacks by manipulating only the APK components most influential to the target model; (ii) a set of fine-grained, build-safe manipulations (including injection and obfuscation of API calls, app modules, permissions, and URLs) with minimal side effects; and (iii) a semantics-preserving functionality test that enforces runtime equivalence by comparing execution logs and API-level traces between the initial and the modified APK. Evaluated on a recent corpus of Android applications, DROIDBREAKER achieves high evasion rates with few queries and minimal side effects in both white-box and black-box settings, and drastically reduces detections by commercial malware scanners hosted on VirusTotal.

  </details>
<br>
**[Over-parameterization and adversarial robustness in neural networks: an overview and empirical analysis](https://link.springer.com/article/10.1007/s44163-026-01621-5)**
  *Authors:* Srishti Gupta, Z Chen, Luca Demetrio, Fabio Brau, Xiaoyi Feng, Zhaoqiang Xia, Antonio Emanuele Ciná, Maura Pintor, Luca Oneto, Ambra Demontis, Battista Biggio, Fabio Roli
  *Published on:* Discover Artificial Intelligence
  <details>
    <summary>Abstract</summary>

Abstract<br>                  Thanks to their extensive capacity, over-parameterized neural networks exhibit superior predictive capabilities and generalization. Nevertheless, having a large parameter space is considered one of the main suspects of the neural network vulnerability to adversarial examples– input samples crafted ad hoc to induce a desired misclassification. The relevant literature has presented contradictory claims regarding the robustness of over-parameterized networks. These contradictory findings might be due to the failure of the attack employed to evaluate the robustness of the networks. Previous research has demonstrated that depending on the considered model, the algorithm employed to generate adversarial examples may not function properly, leading to overestimating its robustness. In this work, we empirically study the robustness of over-parameterized networks against adversarial examples. However, unlike the previous works, we also evaluate the considered attack’s reliability, employing the tools at the state of the art, to support the results’ veracity. Our results show that over-parameterized networks are more robust to adversarial attacks than their under-parameterized counterparts.

  </details>
<br>
**[Adversarial EXEmples: Evasion Attacks Against Machine Learning Windows Malware Detectors](https://www.worldscientific.com/doi/10.1142/9789811262043_0006)**
  *Authors:* Luca Demetrio, Battista Biggio
  *Published on:* Machine Learning for Malware Detection
  <details>
    <summary>Abstract</summary>

(No abstract)

  </details>
<br>
**[Robust Large-Scale Detection of Living-Off-the-Land Reverse Shells via Data Synthesis](https://dl.acm.org/doi/10.1145/3807450)**
  *Authors:* Dmitrijs Trizna, Luca Demetrio, Battista Biggio, Fabio Roli
  *Published on:* ACM Transactions on Privacy and Security
  <details>
    <summary>Abstract</summary>

Living-off-the-land (LOTL) techniques, which exploit legitimate system utilities to execute malicious commands, pose significant challenges to cyber-threat detection by blending with benign behavior. Current state-of-the-art machine learning (ML) detection methods suffer from two critical limitations: (1) a need for large-scale datasets that capture LOTL behaviors, essential for detection at low false-positive rates (FPR) and high true-positive rates (TPR), and (2) a lack of adversarial manipulation evaluations, despite the inherent presence of adaptive attackers in cybersecurity contexts. To address these challenges, we introduce a novel, cyber-security focused data synthesis (DS) framework that augments malicious LOTL samples by combining threat intelligence with legitimate baselines from enterprise networks. We evaluate our framework in a large-scale production environment, focusing on the detection of Linux LOTL reverse shells. The resulting dataset and models—collectively referred to as<br>                    QuasarNix<br>                    —enable ML detectors that detect roughly 60% of malicious reverse shells at an industry-grade FPR = 10<br>                    -6<br>                    , whereas non-augmented baselines remain effectively blind at this operating point. We demonstrate that unprotected ML models remain vulnerable to black-box evasion attacks. To counteract these risks, we incorporate adversarial training into our DS framework, enhancing the robustness of our LOTL detection models. Through an explainability analysis, we confirm that QuasarNix provide detection engineers with evidence-based attribution, aligning with cybersecurity domain expertise. To foster reproducibility, we publicly release our framework implementation,<br>                    <br>                      1<br>                    <br>                    synthesized dataset,<br>                    <br>                      2<br>                    <br>                    and pre-trained models.<br>                    <br>                      3

  </details>
<br>

## 2025
**[Gen-Review: A Large-scale Dataset of AI-Generated (and Human-written) Peer Reviews](https://arxiv.org/abs/2510.21192)**
  *Authors:* Luca Demetrio, Giovanni Apruzzese, Kathrin Grosse, Pavel Laskov, Emil Lupu, Vera Rimmer, Philine Widmer
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

How does the progressive embracement of Large Language Models (LLMs) affect scientific peer reviewing? This multifaceted question is fundamental to the effectiveness -- as well as to the integrity -- of the scientific process. Recent evidence suggests that LLMs may have already been tacitly used in peer reviewing, e.g., at the 2024 International Conference of Learning Representations (ICLR). Furthermore, some efforts have been undertaken in an attempt to explicitly integrate LLMs in peer reviewing by various editorial boards (including that of ICLR'25). To fully understand the utility and the implications of LLMs' deployment for scientific reviewing, a comprehensive relevant dataset is strongly desirable. Despite some previous research on this topic, such dataset has been lacking so far. We fill in this gap by presenting GenReview, the hitherto largest dataset containing LLM-written reviews. Our dataset includes 81K reviews generated for all submissions to the 2018--2025 editions of the ICLR by providing the LLM with three independent prompts: a negative, a positive, and a neutral one. GenReview is also linked to the respective papers and their original reviews, thereby enabling a broad range of investigations. To illustrate the value of GenReview, we explore a sample of intriguing research questions, namely: if LLMs exhibit bias in reviewing (they do); if LLM-written reviews can be automatically detected (so far, they can); if LLMs can rigorously follow reviewing instructions (not always) and whether LLM-provided ratings align with decisions on paper acceptance or rejection (holds true only for accepted papers). GenReview can be accessed at the following link: https://anonymous.4open.science/r/gen_review.

  </details>
<br>
**[Demystifying the Role of Rule-based Detection in AI Systems for Windows Malware Detection](https://ieeexplore.ieee.org/document/11129587/)**
  *Authors:* Andrea Ponte, Luca Demetrio, Luca Oneto, Ivan Tesfai, Battista Biggio, Fabio Roli
  *Published on:* 2025 IEEE European Symposium on Security and Privacy Workshops (EuroS&amp;PW)
  <details>
    <summary>Abstract</summary>

Malware detection increasingly relies on AI systems that integrate signature-based detection with machine learning. However, these components are typically developed and combined in isolation, missing opportunities to reduce data complexity and strengthen defenses against adversarial EXEmples, carefully crafted programs designed to evade detection. Hence, in this work we investigate the influence that signature-based detection exerts on model training, when they are included inside the training pipeline. Specifically, we compare models trained on a comprehensive dataset with an AI system whose machine learning component is trained solely on samples not already flagged by signatures. Our results demonstrate improved robustness to both adversarial EXEmples and temporal data drift, although this comes at the cost of a fixed lower bound on false positives, driven by suboptimal rule selection. We conclude by discussing these limitations and outlining how future research could extend AI-based malware detection to include dynamic analysis, thereby further enhancing system resilience.

  </details>
<br>
**[Evaluating the Evaluators: Trust in Adversarial Robustness Tests](https://arxiv.org/abs/2507.03450)**
  *Authors:* Antonio Emanuele Cinà, Maura Pintor, Luca Demetrio, Ambra Demontis, Battista Biggio, Fabio Roli
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

Despite significant progress in designing powerful adversarial evasion attacks for robustness verification, the evaluation of these methods often remains inconsistent and unreliable. Many assessments rely on mismatched models, unverified implementations, and uneven computational budgets, which can lead to biased results and a false sense of security. Consequently, robustness claims built on such flawed testing protocols may be misleading and give a false sense of security. As a concrete step toward improving evaluation reliability, we present AttackBench, a benchmark framework developed to assess the effectiveness of gradient-based attacks under standardized and reproducible conditions. AttackBench serves as an evaluation tool that ranks existing attack implementations based on a novel optimality metric, which enables researchers and practitioners to identify the most reliable and effective attack for use in subsequent robustness evaluations. The framework enforces consistent testing conditions and enables continuous updates, making it a reliable foundation for robustness verification.

  </details>
<br>
**[Empirical Quantification of Spurious Correlations in Malware Detection](https://arxiv.org/abs/2506.09662)**
  *Authors:* Bianca Perasso, Ludovico Lozza, Andrea Ponte, Luca Demetrio, Luca Oneto, Fabio Roli
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

End-to-end deep learning exhibits unmatched performance for detecting malware, but such an achievement is reached by exploiting spurious correlations -- features with high relevance at inference time, but known to be useless through domain knowledge. While previous work highlighted that deep networks mainly focus on metadata, none investigated the phenomenon further, without quantifying their impact on the decision. In this work, we deepen our understanding of how spurious correlation affects deep learning for malware detection by highlighting how much models rely on empty spaces left by the compiler, which diminishes the relevance of the compiled code. Through our seminal analysis on a small-scale balanced dataset, we introduce a ranking of two end-to-end models to better understand which is more suitable to be put in production.

  </details>
<br>
**[Trust Under Siege: Label Spoofing Attacks against Machine Learning for Android Malware Detection](https://ieeexplore.ieee.org/document/11422270/)**
  *Authors:* Tianwei Lan, Luca Demetrio, Farid Naït‐Abdesselam, Yufei Han, Simone Aonzo
  *Published on:* IEEE Transactions on Information Forensics and Security
  <details>
    <summary>Abstract</summary>

Machine Learning (ML) malware detectors rely heavily on crowd-sourced AntiVirus (AV) labels, with platforms like VirusTotal serving as trusted sources of malware annotations. But what if attackers could manipulate these labels to classify benign software as malicious? We introduce label spoofing attacks, a new threat that contaminates crowd-sourced datasets by embedding minimal and undetectable malicious patterns into benign samples. These patterns coerce AV engines into misclassifying legitimate files as harmful, enabling poisoning attacks against ML-based malware classifiers trained on those data. We demonstrate this scenario by developing AndroVenom, a methodology for polluting realistic data sources and launching subsequent poisoning attacks against ML malware detectors. Experiments show that not only are state-of-the-art feature extractors unable to filter such injections, but various ML models experience Denial-of-Service (DoS) with as little as 1% poisoned samples. Additionally, attackers can flip decisions for specific unaltered benign samples by modifying only 0.015% of the training data, threatening their reputation and market share, while evading anomaly detectors operating on the training data. We conclude by raising concerns about the trustworthiness of ML training processes based on AV annotations and argue that further investigation is needed to develop more reliable labeling strategies.

  </details>
<br>
**[HORNET: Fast and minimal adversarial perturbations](https://linkinghub.elsevier.com/retrieve/pii/S002002552501165X)**
  *Authors:* Jiaping Wu, Antonio Emanuele Ciná, Francesco Villani, Zhaoqiang Xia, Luca Demetrio, Luca Oneto, Davide Anguita, Fabio Roli, Xiaoyi Feng
  *Published on:* Information Sciences
  <details>
    <summary>Abstract</summary>

Fixed-budget attacks aim to generate adversarial examples—carefully crafted inputs designed to induce misclassifications during inference—while adhering to a predefined perturbation budget. These attacks maximize misclassification confidence and benefit from the transferability property, enabling the generated adversarial examples to remain effective even against multiple unknown models. However, to preserve their transferability, such attacks often yield perceptible perturbations, compromising the visual integrity of the adversarial examples. In this paper, we introduce HORNET, an extension of gradient-based fixed-budget attacks designed to minimize the perturbation magnitude of adversarial examples while maintaining their transferability against the target model. HORNET utilizes a distinct source model to craft the adversarial examples and employs a limited number of queries to the unknown target model to further minimize perturbation magnitude. We evaluate HORNET empirically by integrating it with 41 existing attack implementations and testing it against 9 different models, resulting in a total of 1700 unique configurations. Our results demonstrate that HORNET outperforms the state of the art in generating minimally perturbed yet highly transferable adversarial examples across all tested models. Code available at: https://github.com/louiswup/HORNET .

  </details>
<br>

## 2024
**[ModSec-Learn: Boosting ModSecurity with Machine Learning](https://link.springer.com/chapter/10.1007/978-3-031-76459-2_3)**
  *Authors:* Scano, Christian, Floris, Giuseppe, Montaruli, Biagio, Demetrio, Luca, Valenza, Andrea, Compagna, Luca, Ariu, Davide, Piras, Luca, Balzarotti, Davide, Biggio, Battista
  *Published on:* International Symposium on Distributed Computing and Artificial Intelligence
  <details>
    <summary>Abstract</summary>

ModSecurity is widely recognized as the standard open-source Web Application Firewall (WAF), maintained by the OWASP Foundation. It detects malicious requests by matching them against the Core Rule Set (CRS), identifying well-known attack patterns. Each rule is manually assigned a weight based on the severity of the corresponding attack, and a request is blocked if the sum of the weights of matched rules exceeds a given threshold. However, we argue that this strategy is largely ineffective against web attacks, as detection is only based on heuristics and not customized on the application to protect. In this work, we overcome this issue by proposing a machine-learning model that uses the CRS rules as input features. Through training, ModSec-Learn is able to tune the contribution of each CRS rule to predictions, thus adapting the severity level to the web applications to protect. Our experiments show that ModSec-Learn achieves a significantly better trade-off between detection and false positive rates. Finally, we analyze how sparse regularization can reduce the number of rules that are relevant at inference time, by discarding more than 30% of the CRS rules. We release our open-source code and the dataset at <br>                https://github.com/pralab/modsec-learn<br>                <br>               and <br>                https://github.com/pralab/http-traffic-dataset<br>                <br>              , respectively.

  </details>
<br>
**[Over-parameterization and Adversarial Robustness in Neural Networks: An Overview and Empirical Analysis](https://arxiv.org/abs/2406.10090)**
  *Authors:* Srishti Gupta, Zhang Chen, Luca Demetrio, Fabio Brau, Xiaoyi Feng, Zhaoqiang Xia, Antonio Emanuele Cinà, Maura Pintor, Luca Oneto, Ambra Demontis, Battista Biggio, Fabio Roli
  *Published on:* SSRN Electronic Journal
  <details>
    <summary>Abstract</summary>

Thanks to their extensive capacity, over-parameterized neural networks exhibit superior predictive capabilities and generalization. However, having a large parameter space is considered one of the main suspects of the neural networks' vulnerability to adversarial example -- input samples crafted ad-hoc to induce a desired misclassification. Relevant literature has claimed contradictory remarks in support of and against the robustness of over-parameterized networks. These contradictory findings might be due to the failure of the attack employed to evaluate the networks' robustness. Previous research has demonstrated that depending on the considered model, the algorithm employed to generate adversarial examples may not function properly, leading to overestimating the model's robustness. In this work, we empirically study the robustness of over-parameterized networks against adversarial examples. However, unlike the previous works, we also evaluate the considered attack's reliability to support the results' veracity. Our results show that over-parameterized networks are robust against adversarial attacks as opposed to their under-parameterized counterparts.

  </details>
<br>
**[A New Formulation for Zeroth-Order Optimization of Adversarial EXEmples in Malware Detection](https://ieeexplore.ieee.org/document/11316492/)**
  *Authors:* Marco Rando, Luca Demetrio, Lorenzo Rosasco, Fabio Roli
  *Published on:* IEEE Transactions on Information Forensics and Security 21 (2025) 506-515
  <details>
    <summary>Abstract</summary>

Machine learning malware detectors are vulnerable to adversarial EXEmples, i.e., carefully-crafted Windows programs tailored to evade detection. Unlike other adversarial problems, attacks in this context must be functionality-preserving, a constraint that is challenging to address. As a consequence, heuristic algorithms are typically used, which inject new content, either randomly-picked or harvested from legitimate programs. In this paper, we show how learning malware detectors can be cast within a zeroth-order optimization framework, which allows incorporating functionality-preserving manipulations. This permits the deployment of sound and efficient gradient-free optimization algorithms, which come with theoretical guarantees and allow for minimal hyper-parameters tuning. As a by-product, we propose and study ZEXE, a novel zeroth-order attack against Windows malware detection. Compared to state-of-the-art techniques, ZEXE provides improvement in the evasion rate, reducing to less than one third the size of the injected content.

  </details>
<br>
**[SLIFER: Investigating Performance and Robustness of Malware Detection Pipelines](https://linkinghub.elsevier.com/retrieve/pii/S0167404824005704)**
  *Authors:* Andrea Ponte, Dmitrijs Trizna, Luca Demetrio, Battista Biggio, Ivan Tesfai, Fabio Roli
  *Published on:* Computers & Security
  <details>
    <summary>Abstract</summary>

As a result of decades of research, Windows malware detection is approached through a plethora of techniques. However, there is an ongoing mismatch between academia -- which pursues an optimal performances in terms of detection rate and low false alarms -- and the requirements of real-world scenarios. In particular, academia focuses on combining static and dynamic analysis within a single or ensemble of models, falling into several pitfalls like (i) firing dynamic analysis without considering the computational burden it requires; (ii) discarding impossible-to-analyze samples; and (iii) analyzing robustness against adversarial attacks without considering that malware detectors are complemented with more non-machine-learning components. Thus, in this paper we bridge these gaps, by investigating the properties of malware detectors built with multiple and different types of analysis. To do so, we develop SLIFER, a Windows malware detection pipeline sequentially leveraging both static and dynamic analysis, interrupting computations as soon as one module triggers an alarm, requiring dynamic analysis only when needed. Contrary to the state of the art, we investigate how to deal with samples that impede analyzes, showing how much they impact performances, concluding that it is better to flag them as legitimate to not drastically increase false alarms. Lastly, we perform a robustness evaluation of SLIFER. Counter-intuitively, the injection of new content is either blocked more by signatures than dynamic analysis, due to byte artifacts created by the attack, or it is able to avoid detection from signatures, as they rely on constraints on file size disrupted by attacks. As far as we know, we are the first to investigate the properties of sequential malware detectors, shedding light on their behavior in real production environment.

  </details>
<br>
**[Updating Windows Malware Detectors: Balancing Robustness and Regression against Adversarial EXEmples](https://linkinghub.elsevier.com/retrieve/pii/S0167404825001555)**
  *Authors:* Matouš Kozák, Luca Demetrio, Dmitrijs Trizna, Fabio Roli
  *Published on:* Computers & Security. 155 (2025) 104466
  <details>
    <summary>Abstract</summary>

Adversarial EXEmples are carefully-perturbed programs tailored to evade machine learning Windows malware detectors, with an ongoing effort to develop robust models able to address detection effectiveness. However, even if robust models can prevent the majority of EXEmples, to maintain predictive power over time, models are fine-tuned to newer threats, leading either to partial updates or time-consuming retraining from scratch. Thus, even if the robustness against adversarial EXEmples is higher, the new models might suffer a regression in performance by misclassifying threats that were previously correctly detected. For these reasons, we study the trade-off between accuracy and regression when updating Windows malware detectors by proposing EXE-scanner, a plugin that can be chained to existing detectors to promptly stop EXEmples without causing regression. We empirically show that previously proposed hardening techniques suffer a regression of accuracy when updating non-robust models, exacerbating the gap when considering low false positives regimes and temporal drifts affecting data. Also, through EXE-scanner we gain evidence on the detectability of adversarial EXEmples, showcasing the presence of artifacts left inside while creating them. Due to its design, EXE-scanner can be chained to any classifier to obtain the best performance without the need for costly retraining. To foster reproducibility, we openly release the source code, along with the dataset of adversarial EXEmples based on state-of-the-art perturbation algorithms.

  </details>
<br>
**[Certified Adversarial Robustness of Machine Learning-based Malware Detectors via (De)Randomized Smoothing](https://dl.acm.org/doi/10.1145/3827613)**
  *Authors:* Daniel Gibert, Luca Demetrio, Giulio Zizzo, Quan Le, Jordi Planes, Battista Biggio
  *Published on:* ACM Transactions on Privacy and Security
  <details>
    <summary>Abstract</summary>

End-to-end machine learning malware detectors are vulnerable to adversarial EXEmples, carefully-crafted malicious programs that evade detection through minimal perturbations. Such attacks typically operate by either replacing unused content (patch attacks), or injecting new patterns (content-injection attacks). To counter these attacks, recent research has focused on certification methods for end-to-end models that aim to prove robustness guarantees within bounded perturbation sizes. However, existing approaches (i) are not robust against content-injection manipulations and (ii) provide only probabilistic guarantees for perturbations that are negligible relative to the overall program size. Hence, in this article we address these limitations through a novel deterministic certification schema based on (de)randomized smoothing. Our defense splits each executable into non-overlapping chunks and classifies them independently. The final decision is obtained via majority voting across all chunks, ensuring that localized modifications, such as injected or patched code, influence only a limited subset of chunks and have minimal impact in the overall classification. This design guarantees that each chunk either contains or does not contain an adversarial perturbation, enabling us to (i) handle manipulations occurring at arbitrary locations within the program, and (ii) compute deterministic estimates of the perturbation magnitude required to evade detection. We demonstrate the effectiveness of our certification schema through extensive experimental analysis, comparing our defense against a range of state-of-the-art attacks and defenses. The results show that our approach achieves unmatched robustness across all tested attack scenarios, substantially outperforming competing defenses.

  </details>
<br>
**[AttackBench: Evaluating Gradient-based Attacks for Adversarial Examples](https://ojs.aaai.org/index.php/AAAI/article/view/32263)**
  *Authors:* Antonio Emanuele Ciná, Jérôme Rony, Maura Pintor, Luca Demetrio, Ambra Demontis, Battista Biggio, Ismail Ben Ayed, Fabio Roli
  *Published on:* Proceedings of the AAAI Conference on Artificial Intelligence, 39(3), 2600-2608. 2025
  <details>
    <summary>Abstract</summary>

Adversarial examples are typically optimized with gradient-based attacks. While novel attacks are continuously proposed, each is shown to outperform its predecessors using different experimental setups, hyperparameter settings, and number of forward and backward calls to the target models. This provides overly-optimistic and even biased evaluations that may unfairly favor one particular attack over the others. In this work, we aim to overcome these limitations by proposing AttackBench, i.e., the first evaluation framework that enables a fair comparison among different attacks. To this end, we first propose a categorization of gradient-based attacks, identifying their main components and differences. We then introduce our framework, which evaluates their effectiveness and efficiency. We measure these characteristics by (i) defining an optimality metric that quantifies how close an attack is to the optimal solution, and (ii) limiting the number of forward and backward queries to the model, such that all attacks are compared within a given maximum query budget. Our extensive experimental analysis compares more than $100$ attack implementations with a total of over $800$ different configurations against CIFAR-10 and ImageNet models, highlighting that only very few attacks outperform all the competing approaches. Within this analysis, we shed light on several implementation issues that prevent many attacks from finding better solutions or running at all. We release AttackBench as a publicly-available benchmark, aiming to continuously update it to include and evaluate novel gradient-based attacks for optimizing adversarial examples.

  </details>
<br>
**[Robust Synthetic Data-Driven Detection of Living-Off-the-Land Reverse Shells](https://arxiv.org/abs/2402.18329)**
  *Authors:* Dmitrijs Trizna, Luca Demetrio, Battista Biggio, Fabio Roli
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

Living-off-the-land (LOTL) techniques pose a significant challenge to security operations, exploiting legitimate tools to execute malicious commands that evade traditional detection methods. To address this, we present a robust augmentation framework for cyber defense systems as Security Information and Event Management (SIEM) solutions, enabling the detection of LOTL attacks such as reverse shells through machine learning. Leveraging real-world threat intelligence and adversarial training, our framework synthesizes diverse malicious datasets while preserving the variability of legitimate activity, ensuring high accuracy and low false-positive rates. We validate our approach through extensive experiments on enterprise-scale datasets, achieving a 90\% improvement in detection rates over non-augmented baselines at an industry-grade False Positive Rate (FPR) of $10^{-5}$. We define black-box data-driven attacks that successfully evade unprotected models, and develop defenses to mitigate them, producing adversarially robust variants of ML models. Ethical considerations are central to this work; we discuss safeguards for synthetic data generation and the responsible release of pre-trained models across four best performing architectures, including both adversarially and regularly trained variants: https://huggingface.co/dtrizna/quasarnix. Furthermore, we provide a malicious LOTL dataset containing over 1 million augmented attack variants to enable reproducible research and community collaboration: https://huggingface.co/datasets/dtrizna/QuasarNix. This work offers a reproducible, scalable, and production-ready defense against evolving LOTL threats.

  </details>
<br>
**[Robustness-Congruent Adversarial Training for Secure Machine Learning Model Updates](https://arxiv.org/abs/2402.17390)**
  *Authors:* Daniele Angioni, Luca Demetrio, Maura Pintor, Luca Oneto, Davide Anguita, Battista Biggio, Fabio Roli
  *Published on:* IEEE Transactions on Pattern Analysis and Machine Intelligence
  <details>
    <summary>Abstract</summary>

Machine-learning models demand periodic updates to improve their average accuracy, exploiting novel architectures and additional data. However, a newly updated model may commit mistakes the previous model did not make. Such misclassifications are referred to as negative flips, experienced by users as a regression of performance. In this work, we show that this problem also affects robustness to adversarial examples, hindering the development of secure model update practices. In particular, when updating a model to improve its adversarial robustness, previously ineffective adversarial attacks on some inputs may become successful, causing a regression in the perceived security of the system. We propose a novel technique, named robustness-congruent adversarial training, to address this issue. It amounts to fine-tuning a model with adversarial training, while constraining it to retain higher robustness on the samples for which no adversarial example was found before the update. We show that our algorithm and, more generally, learning with non-regression constraints, provides a theoretically-grounded framework to train consistent estimators. Our experiments on robust models for computer vision confirm that both accuracy and robustness, even if improved after model update, can be affected by negative flips, and our robustness-congruent adversarial training can mitigate the problem, outperforming competing baseline methods.

  </details>
<br>

## 2023
**[Raze to the Ground: Query-Efficient Adversarial HTML Attacks on Machine-Learning Phishing Webpage Detectors | Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security](https://dl.acm.org/doi/10.1145/3605764.3623920)**
  *Authors:* Biagio Montaruli, Luca Demetrio, Maura Pintor, Luca Compagna, Davide Balzarotti, Battista Biggio
  *Published on:* Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security
  <details>
    <summary>Abstract</summary>

Machine-learning phishing webpage detectors (ML-PWD) have been shown to suffer from adversarial manipulations of the HTML code of the input webpage. Nevertheless, the attacks recently proposed have demonstrated limited effectiveness due to their lack of optimizing the usage of the adopted manipulations, and they focus solely on specific elements of the HTML code. In this work, we overcome these limitations by first designing a novel set of fine-grained manipulations which allow to modify the HTML code of the input phishing webpage without compromising its maliciousness and visual appearance, i.e., the manipulations are functionality- and rendering-preserving by design. We then select which manipulations should be applied to bypass the target detector by a query-efficient black-box optimization algorithm. Our experiments show that our attacks are able to raze to the ground the performance of current state-of-the-art ML-PWD using just 30 queries, thus overcoming the weaker attacks developed in previous work, and enabling a much fairer robustness evaluation of ML-PWD.

  </details>
<br>
**[Nebula: Self-Attention for Dynamic Malware Analysis](https://ieeexplore.ieee.org/document/10551436/)**
  *Authors:* Dmitrijs Trizna, Luca Demetrio, Battista Biggio, Fabio Roli
  *Published on:* IEEE Transactions on Information Forensics and Security (TIFS) 2024
  <details>
    <summary>Abstract</summary>

Dynamic analysis enables detecting Windows malware by executing programs in a controlled environment and logging their actions. Previous work has proposed training machine learning models, i.e., convolutional and long short-term memory networks, on homogeneous input features like runtime APIs to either detect or classify malware, neglecting other relevant information coming from heterogeneous data like network and file operations. To overcome these issues, we introduce Nebula, a versatile, self-attention Transformer-based neural architecture that generalizes across different behavioral representations and formats, combining diverse information from dynamic log reports. Nebula is composed by several components needed to tokenize, filter, normalize and encode data to feed the transformer architecture. We firstly perform a comprehensive ablation study to evaluate their impact on the performance of the whole system, highlighting which components can be used as-is, and which must be enriched with specific domain knowledge. We perform extensive experiments on both malware detection and classification tasks, using three datasets acquired from different dynamic analyses platforms, show that, on average, Nebula outperforms state-of-the-art models at low false positive rates, with a peak of 12% improvement. Moreover, we showcase how self-supervised learning pre-training matches the performance of fully-supervised models with only 20% of training data, and we inspect the output of Nebula through explainable AI techniques, pinpointing how attention is focusing on specific tokens correlated to malicious activities of malware families. To foster reproducibility, we open-source our findings and models at https://github.com/dtrizna/nebula.

  </details>
<br>
**[Hardening RGB-D Object Recognition Systems against Adversarial Patch Attacks](https://arxiv.org/abs/2309.07106)**
  *Authors:* Yang Zheng, Luca Demetrio, Antonio Emanuele Ciná, Xiaoyi Feng, Zhaoqiang Xia, Zetao Jiang, Ambra Demontis, Battista Biggio, Fabio Roli
  *Published on:* Information Sciences
  <details>
    <summary>Abstract</summary>

RGB-D object recognition systems improve their predictive performances by fusing color and depth information, outperforming neural network architectures that rely solely on colors. While RGB-D systems are expected to be more robust to adversarial examples than RGB-only systems, they have also been proven to be highly vulnerable. Their robustness is similar even when the adversarial examples are generated by altering only the original images' colors. Different works highlighted the vulnerability of RGB-D systems; however, there is a lacking of technical explanations for this weakness. Hence, in our work, we bridge this gap by investigating the learned deep representation of RGB-D systems, discovering that color features make the function learned by the network more complex and, thus, more sensitive to small perturbations. To mitigate this problem, we propose a defense based on a detection mechanism that makes RGB-D systems more robust against adversarial examples. We empirically show that this defense improves the performances of RGB-D systems against adversarial examples even when they are computed ad-hoc to circumvent this detection mechanism, and that is also more effective than adversarial training.

  </details>
<br>
**[ModSec-AdvLearn: Countering Adversarial SQL Injections with Robust Machine Learning](https://ieeexplore.ieee.org/document/11050937/)**
  *Authors:* Giuseppe Floris, Christian Scano, Biagio Montaruli, Luca Demetrio, Andrea Valenza, Luca Compagna, Davide Ariu, Luca Piras, Davide Balzarotti, Battista Biggio
  *Published on:* IEEE Transactions on Information Forensics and Security
  <details>
    <summary>Abstract</summary>

Many Web Application Firewalls (WAFs) leverage the OWASP Core Rule Set (CRS) to block incoming malicious requests. The CRS consists of different sets of rules designed by domain experts to detect well-known web attack patterns. Both the set of rules and the weights used to combine them are manually defined, yielding four different default configurations of the CRS. In this work, we focus on the detection of SQL injection (SQLi) attacks, and show that the manual configurations of the CRS typically yield a suboptimal trade-off between detection and false alarm rates. Furthermore, we show that these configurations are not robust to adversarial SQLi attacks, i.e., carefully-crafted attacks that iteratively refine the malicious SQLi payload by querying the target WAF to bypass detection. To overcome these limitations, we propose (i) using machine learning to automate the selection of the set of rules to be combined along with their weights, i.e., customizing the CRS configuration based on the monitored web services; and (ii) leveraging adversarial training to significantly improve its robustness to adversarial SQLi manipulations. Our experiments, conducted using the well-known open-source ModSecurity WAF equipped with the CRS rules, show that our approach, named ModSec-AdvLearn, can (i) increase the detection rate up to 30%, while retaining negligible false alarm rates and discarding up to 50% of the CRS rules; and (ii) improve robustness against adversarial SQLi attacks up to 85%, marking a significant stride toward designing more effective and robustWAFs.We release our open-source code at https://github.com/pralab/modsec-advlearn.

  </details>
<br>
**[Detecting Attacks Against Deep Reinforcement Learning for Autonomous Driving](https://ieeexplore.ieee.org/document/10327986/)**
  *Authors:* Maura Pintor, Luca Demetrio, Angelo Sotgiu, Hsiao-Ying Lin, Chengfang Fang, Ambra Demontis, Battista Biggio
  *Published on:* 2023 International Conference on Machine Learning and Cybernetics (ICMLC)
  <details>
    <summary>Abstract</summary>

With the advent of deep reinforcement learning, we witness the spread of novel autonomous driving agents that learn how to drive safely among humans. However, skilled attackers might steer the decision-making process of these agents through minimal perturbations applied to the readings of their hardware sensors. These force the behavior of the victim agent to change unexpectedly, increasing the likelihood of crashes by inhibiting its braking capability or coercing it into constantly changing lanes. To counter these phenomena, we propose a detector that can be mounted on autonomous driving cars to spot the presence of ongoing attacks. The detector first profiles the agent's behavior without attacks by looking at the representation learned during training. Once deployed, the detector discards all the decisions that deviate from the regular driving pattern. We empirically highlight the detection capabilities of our work by testing it against unseen attacks deployed with increasing strength.

  </details>
<br>

## 2022
**[Security of Deep Reinforcement Learning for Autonomous Driving: A Survey](https://arxiv.org/abs/2212.06123v4)**
  *Authors:* Ambra Demontis, Maura Pintor, Srishti Gupta, Luca Demetrio, Kathrin Grosse, Hsiao-Ying Lin, Chengfang Fang, Battista Biggio, Fabio Roli
  *Published on:* arXiv (Cornell University)
  <details>
    <summary>Abstract</summary>

Reinforcement learning (RL) enables agents to learn optimal behaviors through interaction with their environment and has been increasingly deployed in safety-critical applications, including autonomous driving. Despite its promise, RL is susceptible to attacks designed either to compromise policy learning or to induce erroneous decisions by trained agents. Although the literature on RL security has grown rapidly and several surveys exist, existing categorizations often fall short in guiding the selection of appropriate defenses for specific systems. In this work, we present a comprehensive survey of 86 recent studies on RL security, addressing these limitations by systematically categorizing attacks and defenses according to defined threat models and single- versus multi-agent settings. Furthermore, we examine the relevance and applicability of state-of-the-art attacks and defense mechanisms within the context of autonomous driving, providing insights to inform the design of robust RL systems.

  </details>
<br>
**[Explaining Machine Learning DGA Detectors from DNS Traffic Data](https://arxiv.org/abs/2208.05285)**
  *Authors:* Giorgio Piras, Maura Pintor, Luca Demetrio, Battista Biggio
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

One of the most common causes of lack of continuity of online systems stems from a widely popular Cyber Attack known as Distributed Denial of Service (DDoS), in which a network of infected devices (botnet) gets exploited to flood the computational capacity of services through the commands of an attacker. This attack is made by leveraging the Domain Name System (DNS) technology through Domain Generation Algorithms (DGAs), a stealthy connection strategy that yet leaves suspicious data patterns. To detect such threats, advances in their analysis have been made. For the majority, they found Machine Learning (ML) as a solution, which can be highly effective in analyzing and classifying massive amounts of data. Although strongly performing, ML models have a certain degree of obscurity in their decision-making process. To cope with this problem, a branch of ML known as Explainable ML tries to break down the black-box nature of classifiers and make them interpretable and human-readable. This work addresses the problem of Explainable ML in the context of botnet and DGA detection, which at the best of our knowledge, is the first to concretely break down the decisions of ML classifiers when devised for botnet/DGA detection, therefore providing global and local explanations.

  </details>
<br>
**[Robust Machine Learning for Malware Detection over Time](https://arxiv.org/abs/2208.04838)**
  *Authors:* Daniele Angioni, Luca Demetrio, Maura Pintor, Battista Biggio
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

The presence and persistence of Android malware is an on-going threat that plagues this information era, and machine learning technologies are now extensively used to deploy more effective detectors that can block the majority of these malicious programs. However, these algorithms have not been developed to pursue the natural evolution of malware, and their performances significantly degrade over time because of such concept-drift. Currently, state-of-the-art techniques only focus on detecting the presence of such drift, or they address it by relying on frequent updates of models. Hence, there is a lack of knowledge regarding the cause of the concept drift, and ad-hoc solutions that can counter the passing of time are still under-investigated. In this work, we commence to address these issues as we propose (i) a drift-analysis framework to identify which characteristics of data are causing the drift, and (ii) SVM-CB, a time-aware classifier that leverages the drift-analysis information to slow down the performance drop. We highlight the efficacy of our contribution by comparing its degradation over time with a state-of-the-art classifier, and we show that SVM-CB better withstands the distribution changes that naturally characterize the malware domain. We conclude by discussing the limitations of our approach and how our contribution can be taken as a first step towards more time-resistant classifiers that not only tackle, but also understand the concept drift that affects data.

  </details>
<br>
**[Practical Attacks on Machine Learning: A Case Study on Adversarial Windows Malware](https://ieeexplore.ieee.org/document/9817418/)**
  *Authors:* Luca Demetrio, Battista Biggio, Fabio Roli
  *Published on:* IEEE Security & Privacy, 2022
  <details>
    <summary>Abstract</summary>

While machine learning is vulnerable to adversarial examples, it still lacks systematic procedures and tools for evaluating its security in different application contexts. In this article, we discuss how to develop automated and scalable security evaluations of machine learning using practical attacks, reporting a use case on Windows malware detection.

  </details>
<br>
**[Phantom Sponges: Exploiting Non-Maximum Suppression to Attack Deep Object Detectors](https://arxiv.org/abs/2205.13618)**
  *Authors:* Avishag Shapira, Alon Zolfi, Luca Demetrio, Battista Biggio, Asaf Shabtai
  *Published on:* IEEE Winter Conference on Applications of Computer Vision
  <details>
    <summary>Abstract</summary>

Adversarial attacks against deep learning-based object detectors have been studied extensively in the past few years. Most of the attacks proposed have targeted the model's integrity (i.e., caused the model to make incorrect predictions), while adversarial attacks targeting the model's availability, a critical aspect in safety-critical domains such as autonomous driving, have not yet been explored by the machine learning research community. In this paper, we propose a novel attack that negatively affects the decision latency of an end-to-end object detection pipeline. We craft a universal adversarial perturbation (UAP) that targets a widely used technique integrated in many object detector pipelines -- non-maximum suppression (NMS). Our experiments demonstrate the proposed UAP's ability to increase the processing time of individual frames by adding "phantom" objects that overload the NMS algorithm while preserving the detection of the original objects which allows the attack to go undetected for a longer period of time.

  </details>
<br>
**[ImageNet-Patch: A Dataset for Benchmarking Machine Learning Robustness against Adversarial Patches](https://linkinghub.elsevier.com/retrieve/pii/S0031320322005441)**
  *Authors:* Maura Pintor, Daniele Angioni, Angelo Sotgiu, Luca Demetrio, Ambra Demontis, Battista Biggio, Fabio Roli
  *Published on:* Pattern Recognition
  <details>
    <summary>Abstract</summary>

Adversarial patches are optimized contiguous pixel blocks in an input image that cause a machine-learning model to misclassify it. However, their optimization is computationally demanding, and requires careful hyperparameter tuning, potentially leading to suboptimal robustness evaluations. To overcome these issues, we propose ImageNet-Patch, a dataset to benchmark machine-learning models against adversarial patches. It consists of a set of patches, optimized to generalize across different models, and readily applicable to ImageNet data after preprocessing them with affine transformations. This process enables an approximate yet faster robustness evaluation, leveraging the transferability of adversarial perturbations. We showcase the usefulness of this dataset by testing the effectiveness of the computed patches against 127 models. We conclude by discussing how our dataset could be used as a benchmark for robustness, and how our methodology can be generalized to other domains. We open source our dataset and evaluation code at https://github.com/pralab/ImageNet-Patch.

  </details>
<br>
**[Practical Evaluation of Poisoning Attacks on Online Anomaly Detectors in Industrial Control Systems](https://linkinghub.elsevier.com/retrieve/pii/S0167404822002942)**
  *Authors:* Moshe Kravchik, Luca Demetrio, Battista Biggio, Asaf Shabtai
  *Published on:* Computers & Security
  <details>
    <summary>Abstract</summary>

(No abstract)

  </details>
<br>
**[Towards learning trustworthily, automatically, and with guarantees on graphs: An overview](https://linkinghub.elsevier.com/retrieve/pii/S0925231222004520)**
  *Authors:* Luca Oneto, Nicolò Navarin, Battista Biggio, Federico Errica, Alessio Micheli, Franco Scarselli, Monica Bianchini, Luca Demetrio, Pietro Bongini, Armando Tacchella, Alessandro Sperduti
  *Published on:* Neurocomputing
  <details>
    <summary>Abstract</summary>

(No abstract)

  </details>
<br>
**[Secml: Secure and Explainable Machine Learning in Python](https://www.ssrn.com/abstract=4003262)**
  *Authors:* Marco Melis, Ambra Demontis, Maura Pintor, Angelo Sotgiu, Luca Demetrio, Battista Biggio
  *Published on:* SSRN Electronic Journal
  <details>
    <summary>Abstract</summary>

We present secml, an open-source Python library for secure and explainable machine learning. It implements the most popular attacks against machine learning, including not only test-time evasion attacks to generate adversarial examples against deep neural networks, but also training-time poisoning attacks against support vector machines and many other algorithms. These attacks enable evaluating the security of learning algorithms and of the corresponding defenses under both white-box and black-box threat models. To this end, secml provides built-in functions to compute security evaluation curves, showing how quickly classification performance decreases against increasing adversarial perturbations of the input data. secml also includes explainability methods to help understand why adversarial attacks succeed against a given model, by visualizing the most influential features and training prototypes contributing to each decision. It is distributed under the Apache License 2.0, and hosted at https://gitlab.com/pralab/secml.

  </details>
<br>

## 2021
**[Indicators of Attack Failure: Debugging and Improving Optimization of Adversarial Examples](https://arxiv.org/abs/2106.09947)**
  *Authors:* Maura Pintor, Luca Demetrio, Angelo Sotgiu, Ambra Demontis, Nicholas Carlini, Battista Biggio, Fabio Roli
  *Published on:* neural information processing systems
  <details>
    <summary>Abstract</summary>

Evaluating robustness of machine-learning models to adversarial examples is a challenging problem. Many defenses have been shown to provide a false sense of robustness by causing gradient-based attacks to fail, and they have been broken under more rigorous evaluations. Although guidelines and best practices have been suggested to improve current adversarial robustness evaluations, the lack of automatic testing and debugging tools makes it difficult to apply these recommendations in a systematic manner. In this work, we overcome these limitations by: (i) categorizing attack failures based on how they affect the optimization of gradient-based attacks, while also unveiling two novel failures affecting many popular attack implementations and past evaluations; (ii) proposing six novel indicators of failure, to automatically detect the presence of such failures in the attack optimization process; and (iii) suggesting a systematic protocol to apply the corresponding fixes. Our extensive experimental analysis, involving more than 15 models in 3 distinct application domains, shows that our indicators of failure can be used to debug and improve current adversarial robustness evaluations, thereby providing a first concrete step towards automatizing and systematizing them. Our open-source code is available at: https://github.com/pralab/IndicatorsOfAttackFailure.

  </details>
<br>
**[secml-malware: Pentesting Windows Malware Classifiers with Adversarial EXEmples in Python](https://arxiv.org/abs/2104.12848)**
  *Authors:* Luca Demetrio, Battista Biggio
  *Published on:* SSRN Electronic Journal
  <details>
    <summary>Abstract</summary>

Machine learning has been increasingly used as a first line of defense for Windows malware detection. Recent work has however shown that learning-based malware detectors can be evaded by carefully-perturbed input malware samples, referred to as adversarial EXEmples, thus demanding for tools that can ease and automate the adversarial robustness evaluation of such detectors. To this end, we present secml-malware, the first Python library for computing adversarial attacks on Windows malware detectors. secml-malware implements state-of-the-art white-box and black-box attacks on Windows malware classifiers, by leveraging a set of feasible manipulations that can be applied to Windows programs while preserving their functionality. The library can be used to perform the penetration testing and assessment of the adversarial robustness of Windows malware detectors, and it can be easily extended to include novel attack strategies. Our library is available at https://github.com/pralab/secml_malware.

  </details>
<br>
**[secml-malware: A Python Library for Adversarial Robustness Evaluation of Windows Malware Classifiers.](https://arxiv.org/abs/2104.12848)**
  *Authors:* Luca Demetrio, Battista Biggio
  *Published on:* arXiv (Cornell University)
  <details>
    <summary>Abstract</summary>

Machine learning has been increasingly used as a first line of defense for Windows malware detection. Recent work has however shown that learning-based malware detectors can be evaded by carefully-perturbed input malware samples, referred to as adversarial EXEmples, thus demanding for tools that can ease and automate the adversarial robustness evaluation of such detectors. To this end, we present secml-malware, the first Python library for computing adversarial attacks on Windows malware detectors. secml-malware implements state-of-the-art white-box and black-box attacks on Windows malware classifiers, by leveraging a set of feasible manipulations that can be applied to Windows programs while preserving their functionality. The library can be used to perform the penetration testing and assessment of the adversarial robustness of Windows malware detectors, and it can be easily extended to include novel attack strategies. Our library is available at https://github.com/pralab/secml_malware.

  </details>
<br>
**[Slope: A First-order Approach for Measuring Gradient Obfuscation](https://www.esann.org/sites/default/files/proceedings/2021/ES2021-99.pdf)**
  *Authors:* Maura Pintor, Luca Demetrio, Giovanni Manca, Battista Biggio, Fabio Roli
  *Published on:* European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning (ESANN)
  <details>
    <summary>Abstract</summary>

Evaluating adversarial robustness is a challenging problem.Many defenses have been shown to provide a false sense of security by unintentionally obfuscating gradients, hindering the optimization process of gradient-based attacks.Such defenses have been subsequently shown to fail against adaptive attacks crafted to circumvent gradient obfuscation.In this work, we present Slope, a metric that detects obfuscated gradients by comparing the expected and the actual increase of the attack loss after one iteration.We show that our metric can detect the presence of obfuscated gradients in many documented cases, providing a useful debugging tool towards improving adversarial robustness evaluations.

  </details>
<br>

## 2020
**[Adversarial EXEmples: A Survey and Experimental Evaluation of Practical Attacks on Machine Learning for Windows Malware Detection](https://dl.acm.org/doi/10.1145/3473039)**
  *Authors:* Luca Demetrio, Scott E. Coull, Battista Biggio, Giovanni Lagorio, Alessandro Armando, Fabio Roli
  *Published on:* ACM Transactions on Privacy and Security (TOPS)
  <details>
    <summary>Abstract</summary>

Recent work has shown that adversarial Windows malware samples—referred to as adversarial<br>                    EXE<br>                    mples in this article—can bypass machine learning-based detection relying on static code analysis by perturbing relatively few input bytes. To preserve malicious functionality, previous attacks either add bytes to existing non-functional areas of the file, potentially limiting their effectiveness, or require running computationally demanding validation steps to discard malware variants that do not correctly execute in sandbox environments. In this work, we overcome these limitations by developing a unifying framework that does not only encompass and generalize previous attacks against machine-learning models, but also includes three novel attacks based on practical, functionality-preserving manipulations to the Windows Portable Executable file format. These attacks, named<br>                    Full DOS<br>                    ,<br>                    Extend<br>                    , and<br>                    Shift<br>                    , inject the adversarial payload by respectively manipulating the DOS header, extending it, and shifting the content of the first section. Our experimental results show that these attacks outperform existing ones in both white-box and black-box scenarios, achieving a better tradeoff in terms of evasion rate and size of the injected payload, while also enabling evasion of models that have been shown to be robust to previous attacks. To facilitate reproducibility of our findings, we open source our framework and all the corresponding attack implementations as part of the secml-malware Python library. We conclude this work by discussing the limitations of current machine learning-based malware detectors, along with potential mitigation strategies based on embedding domain knowledge coming from subject-matter experts directly into the learning process.

  </details>
<br>
**[Functionality-preserving Black-box Optimization of Adversarial Windows Malware](https://ieeexplore.ieee.org/document/9437194/)**
  *Authors:* Luca Demetrio, Battista Biggio, Giovanni Lagorio, Fabio Roli, Alessandro Armando
  *Published on:* IEEE Transactions on Information Forensics and Security
  <details>
    <summary>Abstract</summary>

Windows malware detectors based on machine learning are vulnerable to adversarial examples, even if the attacker is only given black-box query access to the model. The main drawback of these attacks is that: (i) they are query-inefficient, as they rely on iteratively applying random transformations to the input malware; and (ii) they may also require executing the adversarial malware in a sandbox at each iteration of the optimization process, to ensure that its intrusive functionality is preserved. In this paper, we overcome these issues by presenting a novel family of black-box attacks that are both query-efficient and functionality-preserving, as they rely on the injection of benign content - which will never be executed - either at the end of the malicious file, or within some newly-created sections. Our attacks are formalized as a constrained minimization problem which also enables optimizing the trade-off between the probability of evading detection and the size of the injected payload. We empirically investigate this trade-off on two popular static Windows malware detectors, and show that our black-box attacks can bypass them with only few queries and small payloads, even when they only return the predicted labels. We also evaluate whether our attacks transfer to other commercial antivirus solutions, and surprisingly find that they can evade, on average, more than 12 commercial antivirus engines. We conclude by discussing the limitations of our approach, and its possible future extensions to target malware classifiers based on dynamic analysis.

  </details>
<br>
**[WAF-A-MoLE: Evading Web Application Firewalls through Adversarial Machine Learning](https://dl.acm.org/doi/10.1145/3341105.3373962)**
  *Authors:* Luca Demetrio, Andrea Valenza, Gabriele Costa, Giovanni Lagorio
  *Published on:* Proceedings of the 35th Annual ACM Symposium on Applied Computing 2020
  <details>
    <summary>Abstract</summary>

Web Application Firewalls are widely used in production environments to mitigate security threats like SQL injections. Many industrial products rely on signature-based techniques, but machine learning approaches are becoming more and more popular. The main goal of an adversary is to craft semantically malicious payloads to bypass the syntactic analysis performed by a WAF. In this paper, we present WAF-A-MoLE, a tool that models the presence of an adversary. This tool leverages on a set of mutation operators that alter the syntax of a payload without affecting the original semantics. We evaluate the performance of the tool against existing WAFs, that we trained using our publicly available SQL query dataset. We show that WAF-A-MoLE bypasses all the considered machine learning based WAFs.

  </details>
<br>
**[Efficient Black-box Optimization of Adversarial Windows Malware with Constrained Manipulations.](https://arxiv.org/pdf/2003.13526)**
  *Authors:* Luca Demetrio, Battista Biggio, Giovanni Lagorio, Fabio Roli, Alessandro Armando
  *Published on:* arXiv (Cornell University)
  <details>
    <summary>Abstract</summary>

Windows malware detectors based on machine learning are vulnerable to adversarial examples, even if the attacker is only given black-box access to the model. The main drawback of these attacks is that they require executing the adversarial malware sample in a sandbox at each iteration of its optimization process, to ensure that its intrusive functionality is preserved. In this paper, we present a novel black-box attack that leverages a set of semantics-preserving, constrained malware manipulations to overcome this computationally-demanding validation step. Our attack is formalized as a constrained minimization problem which also enables optimizing the trade-off between the probability of evading detection and the size of the injected adversarial payload. We investigate this trade-off empirically, on two popular static Windows malware detectors, and show that our black-box attack is able to bypass them with only few iterations and changes. We also evaluate whether our attack transfers to other commercial antivirus solutions, and surprisingly find that it can increase the probability of evading some of them. We conclude by discussing the limitations of our approach, and its possible future extensions to target malware classifiers based on dynamic analysis.

  </details>
<br>

## 2019
**[secml: A Python Library for Secure and Explainable Machine Learning](https://linkinghub.elsevier.com/retrieve/pii/S2352711022000656)**
  *Authors:* Maura Pintor, Luca Demetrio, Angelo Sotgiu, Marco Melis, Ambra Demontis, Battista Biggio
  *Published on:* SoftwareX 18 (2022)
  <details>
    <summary>Abstract</summary>

We present \texttt{secml}, an open-source Python library for secure and explainable machine learning. It implements the most popular attacks against machine learning, including test-time evasion attacks to generate adversarial examples against deep neural networks and training-time poisoning attacks against support vector machines and many other algorithms. These attacks enable evaluating the security of learning algorithms and the corresponding defenses under both white-box and black-box threat models. To this end, \texttt{secml} provides built-in functions to compute security evaluation curves, showing how quickly classification performance decreases against increasing adversarial perturbations of the input data. \texttt{secml} also includes explainability methods to help understand why adversarial attacks succeed against a given model, by visualizing the most influential features and training prototypes contributing to each decision. It is distributed under the Apache License 2.0 and hosted at \url{https://github.com/pralab/secml}.

  </details>
<br>
**[Explaining Vulnerabilities of Deep Learning to Adversarial Malware Binaries](https://arxiv.org/abs/1901.03583)**
  *Authors:* Luca Demetrio, Battista Biggio, Giovanni Lagorio, Fabio Roli, Alessandro Armando
  *Published on:* arXiv
  <details>
    <summary>Abstract</summary>

Recent work has shown that deep-learning algorithms for malware detection are also susceptible to adversarial examples, i.e., carefully-crafted perturbations to input malware that enable misleading classification. Although this has questioned their suitability for this task, it is not yet clear why such algorithms are easily fooled also in this particular application domain. In this work, we take a first step to tackle this issue by leveraging explainable machine-learning algorithms developed to interpret the black-box decisions of deep neural networks. In particular, we use an explainable technique known as feature attribution to identify the most influential input features contributing to each decision, and adapt it to provide meaningful explanations to the classification of malware binaries. In this case, we find that a recently-proposed convolutional neural network does not learn any meaningful characteristic for malware detection from the data and text sections of executable files, but rather tends to learn to discriminate between benign and malware samples based on the characteristics found in the file header. Based on this finding, we propose a novel attack algorithm that generates adversarial malware binaries by only changing few tens of bytes in the file header. With respect to the other state-of-the-art attack algorithms, our attack does not require injecting any padding bytes at the end of the file, and it is much more efficient, as it requires manipulating much fewer bytes.

  </details>
<br>
**[WAF-A-MoLE: An adversarial tool for assessing ML-based WAFs](https://linkinghub.elsevier.com/retrieve/pii/S2352711019302997)**
  *Authors:* Andrea Valenza, Luca Demetrio, Gabriele Costa, Giovanni Lagorio
  *Published on:* SoftwareX
  <details>
    <summary>Abstract</summary>

Web Application Firewalls (WAFs) are plug-and-play security gateways that promise to enhance the security of a (potentially vulnerable) system with minimal cost and configuration. In recent years, machine learning-based WAFs are catching up with traditional, signature-based ones. They are competitive because they do not require predefined rules; instead, they infer their rules through a learning process. In this paper, we present WAF-A-MoLE, a WAF breaching tool. It uses guided mutational-based fuzzing to generate adversarial examples. The main applications include WAF ( i ) penetration testing, ( i i ) benchmarking and ( i i i ) hardening.

  </details>
<br>
**[ZenHackAdemy: Ethical Hacking @ DIBRIS](https://www.scitepress.org/Link.aspx?doi=10.5220/0007747104050413)**
  *Authors:* Luca Demetrio, Giovanni Lagorio, Marina Ribaudo, Enrico Russo, Andrea Valenza
  *Published on:* Proceedings of the 11th International Conference on Computer Supported Education
  <details>
    <summary>Abstract</summary>

Cybersecurity attacks are on the rise, and the current response is not effective enough. The need for a competent workforce, able to face attackers, is increasing. At the moment, the gap between academia and real-world skills is huge and academia cannot provide students with skills that match those of an attacker. To pass on these skills, teachers have to train students in scenarios as close as possible to real-world ones. Capture the Flag (CTF) competitions are a great tool to achieve this goal, since they encourage students to think as an attacker does, thus creating more awareness on the modalities and consequences of an attack. We describe our experience in running an educational activity on ethical hacking, which we proposed to computer science and computer engineering students. We organized seminars, outside formal classes, and provided online support on the hands-on part of the training. We delivered different types of exercises and held a final CTF competition. These activities resulted in growing a community of students and researchers interested in cybersecurity, and some of them have formed ZenHack, an official CTF team.

  </details>
<br>
