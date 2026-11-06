# r/place as a model organism

Our field struggles to build cumulative knowledge (Pfeffer, 1993; Davis, 2010). Part of the problem is ontological. As March said, "God gave all the easy problems to the physicists" (Dong et al., 2017:12), meaning that organizations are complex, change while we study them, rarely allow experiments, and confound skill with chance. Another part comes from our practices. Our promotion systems institutionalize a "general call to publish or perish" (Aguinis et al., 2020:136). Our journals urge us to "examine outliers (Lewin [1992]) rather than central tendencies" (Daft & Lewin, 1990:6). Jointly, ontology and practice promote the "search for novelty rather than truth" (Barley, 2016:5), leading our field "toward an equilibrium of more rather than better research" (Gartenberg et al., 2026a:795).

## Claims faster than we relate them

Hence, our field produces claims faster than it relates them: a problem of "disorganization, not amount" (Cronin et al., 2021:668). Biology faced the same problem when genome sequencing in the early 2000s produced thousands of claims about gene function (Adams et al., 2000). Each claim met a filter: does it hold in a model organism? Databases grew around each organism (Leonelli, 2016), and researchers judged new claims against everything known about it. "As genetics needs its model organisms, its Drosophila and Neurospora, so [Organization Science] needs standard task environments around which knowledge and understanding can cumulate" (Simon & Chase, 1973:394). Yet we lack a model organism. A model organism is "standardized to fit an integrative and comparative mode of research" (Ankeny & Leonelli, 2011:313): standardized specimens, shared data and tools, and a community working toward an integrated account of the organism. The aim is to understand how its processes connect and which findings extend to other organisms.

## One account of the organism

Model organisms let separate studies build one account of the same organism (Ankeny & Leonelli, 2011). Research on the fruit fly relates genetics, development and physiology within the whole organism (Adams et al., 2000). r/place has so far been studied in parts. Rappaz et al. (2018) examined collaboration among users, Israeli et al. (2022) community participation, and Jemine (2025) coordination in four communities. Each answers its own question, and nothing yet relates their findings.

As a model organism, r/place turns these studies into parts of one agenda, which asks how communities recruit members, coordinate work, maintain artworks and deal with their neighbors. Our instrument composes coded accounts of 705 curated communities into a population model in which these processes appear as parts of the same organizing ([integrative understanding](#integrative-understanding)). Later studies can place their findings against this baseline.

## Three examples and r/place

Table 1 of the Technical Appendix compares r/place with the fruit fly and with two research objects outside biology, chess and ImageNet 2012. Its rows adapt four features that Ankeny and Leonelli (2011) discuss in model organism research. Material accessibility means that researchers can obtain and examine the same material. Integrative understanding means that studies of different processes add to one account of the whole organism. Standardization means that shared conditions make specimens or cases comparable. A research community shares materials, methods and results, so later work can revisit and revise earlier findings. Chess (Simon & Chase, 1973) and ImageNet (Deng et al., 2009) show that research objects built by people can carry some of these features, though ImageNet supports common evaluation more than integration across phenomena. Each column shows how one research object meets the four features. The sections below take them in turn for r/place; [the instrument](instrument.html) has its own page.

On a small screen, scroll the table sideways to compare fields.

| Characteristic | Fruit fly | Chess | ImageNet 2012 | r/place |
|---|---|---|---|---|
| **Field** | Genetics | Cognitive psychology | Machine learning | Organization science |
| **Material accessibility** | Standard fly strains that laboratories obtain, breed and examine. | A game with explicit rules, recorded positions and recorded games. | Labeled images in 1,000 categories, available for research download. | Public records of pixel changes and Reddit discussions. |
| **Integrative understanding** | Relates genetics, development and physiology within the whole organism. | Relates perception, memory and search in skilled play. | Compares classification and localization methods on a shared image collection. | Relates recruitment, coordination, maintenance and relations among communities. |
| **Standardization** | Standard strains and shared protocols make specimens comparable. | Fixed rules and measurable differences in skill. | Agreed labels, data splits and evaluation rules. | Shared event rules; coding contracts held constant within a run. |
| **Research community** | Stock centers and FlyBase support sharing specimens, methods and results. | Published position tasks and game records let later work revisit findings. | Development kits and a public challenge put new methods to common tests. | Shared coded cases, contracts and checkpoints invite reuse and revision. |

## Material accessibility

The 72-hour event provides a bounded record of communities forming, building and defending artworks. Reddit discussions can be read alongside pixel changes ([the record in numbers](data.html)). Researchers can return to the same evidence instead of relying only on published accounts. LLM agents reduce the cost of reading the 705 communities' records ([community coding](how-coding-works.html)). The dataset is frozen, but researchers can change the instrument, use another literature or broaden the census within the dataset.

The record also has gaps. It covers Reddit discussions and pixel changes, but not the Discord servers where some communities also met. The census starts from the curated atlas of the finished canvas. A community whose artwork was wholly erased enters only if a surviving artwork also credits it, so failure is undersampled (Denrell, 2003; [the census](census.html)).

## Integrative understanding

The aim is to relate processes that separate studies can examine on their own. From our preliminary findings, we observe that recruitment, coordination, maintenance and relations with neighbors form distinctive roles in how communities organize ([the eight dimensions](results/population-aggregation.html#eight-aggregate-dimensions); [the forms](results/population-forms.html)). The current model provides a basis for comparison with open-source communities and self-managing firms (O'Mahony & Ferraro, 2007; Lee & Edmondson, 2017). Few communities show a clear signal of authority, such as a leader, a vote, an oath, a sanction or a division of work. The coders found one in 44 of the 705 communities while coding, and in about 119 when the returned model asked the community coders to check explicitly for it ([how each count is made](results/population-aggregation.html#decided-order)). These indicators describe different arrangements and do not form a single measure of formal authority. Extending the model to hierarchical firms requires further evidence. Later researchers can examine other connections or challenge those proposed.

## Standardization

All communities worked under the same pixel-placement rules: each user could change one pixel's color every five minutes, and anyone could overwrite it (Simpson et al., 2017). Communities nevertheless differed in their histories and circumstances. We held the coders' contract constant within a run ([versions](versions.html)). Later runs can change a specified component, such as the literature, community coder or aggregator, and compare the results with the baseline. The 298 communities coded on two LLMs give a first measure of variation between models. A planned run with an open-weight model will extend that comparison and lower the cost of replication.

## Research community

A model organism becomes a common research resource through sustained sharing and reuse (Ankeny & Leonelli, 2011; Kohler, 1994). We provide the baseline, coded cases and tools for inspecting the analysis. Stable identifiers link claims back to their evidence, so later researchers can compare, revise or replace accounts and share the changes. This provides infrastructure for a research community; whether one forms depends on others adopting and extending it. Researchers can rerun the instrument ([run the study](run.html)) or resume it from a [checkpoint](interviews.html), then return a revised population model to the community coders to assess its fit to their cases.

Start with the [data guide](guides/download.html), read the [completed model, form accounts and audits](guides/study.html), or check a claim against the [full reference](reference.html), which holds the source documents and their hashes.

## An open-ended program

The dataset is frozen. But the instrument can change: the model can improve by changing the literature, broadening the census, or checking how novel mechanisms increase our understanding of r/place. This model organism is an "open-ended program of research" (Lewin & Volberda, 1999:529) in which later models are judged against the baseline, including where they revise or reject it. The call for this special issue asks "what kinds of knowledge can we create when the tools of inquiry themselves change?" (Gartenberg et al., 2026b:2). We address this question by composing case accounts into a population model that preserves their differences.

As with biology's understanding of the fruit fly, our understanding of what happened during r/place 2017 will grow over time. A model organism does not forbid outliers or novelty. It gives them a baseline to be measured against. Machlup's constraints were an economist's excuse to disregard the behavior of organizations. Organization Science has no such excuse: it "was founded as a bet on escaping the constraints of local search and incrementalism" (Gartenberg et al., 2026b:1). Whether our field "evolves toward 'more' or 'better'" is an institutional question (Gartenberg et al., 2026a:811), and a model organism is a nudge toward "better".

## Inspect the examples

- Fruit fly: [Ankeny and Leonelli's analysis](https://doi.org/10.1016/j.shpsa.2010.11.039) and the [Bloomington stock center](https://bdsc.indiana.edu/about/index.html).
- Chess: [Simon and Chase, Skill in chess (1973)](https://iiif.library.cmu.edu/file/Simon_box00066_fld05052_bdl0001_doc0001/Simon_box00066_fld05052_bdl0001_doc0001.pdf).
- ImageNet: [the 2012 challenge's tasks and evaluation rules](https://ftp.image-net.org/challenges/LSVRC/2012/index.php).
- r/place: [the data collection](sources/data-README.html), [the study and its limits](guides/study.html), and [one claim traced to its evidence](records/example-PlaceNL.html).

## References

Adams, M. D., et al. (2000). The genome sequence of Drosophila melanogaster. *Science*, 287(5461), 2185–2195.

Aguinis, H., Cummings, C., Ramani, R. S., & Cummings, T. G. (2020). "An A is an A": The new bottom line for valuing academic research. *Academy of Management Perspectives*, 34(1), 135–154.

Ankeny, R. A., & Leonelli, S. (2011). What's so special about model organisms? *Studies in History and Philosophy of Science Part A*, 42(2), 313–323.

Barley, S. R. (2016). 60th anniversary essay: Ruminations on how we became a mystery house and how we might get out. *Administrative Science Quarterly*, 61(1), 1–8.

Cronin, M. A., Stouten, J., & van Knippenberg, D. (2021). The theory crisis in management research: Solving the right problem. *Academy of Management Review*, 46(4), 667–683.

Daft, R. L., & Lewin, A. Y. (1990). Can organization studies begin to break out of the normal science straitjacket? An editorial essay. *Organization Science*, 1(1), 1–9.

Davis, G. F. (2010). Do theories of organizations progress? *Organizational Research Methods*, 13(4), 690–709.

Denrell, J. (2003). Vicarious learning, undersampling of failure, and the myths of management. *Organization Science*, 14(3), 227–243.

Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., & Fei-Fei, L. (2009). ImageNet: A large-scale hierarchical image database. In *2009 IEEE Conference on Computer Vision and Pattern Recognition* (pp. 248–255). IEEE.

Dong, J., March, J. G., & Workiewicz, M. (2017). On organizing: An interview with James G. March. *Journal of Organization Design*, 6, 14.

Gartenberg, C., Hasan, S., Murray, A., & Pierce, L. (2026a). More versus better: Artificial intelligence, incentives, and the emerging crisis in peer review. *Organization Science*, 37(3), 795–812.

Gartenberg, C., Hasan, S., Pierce, L., Bail, C., Dai, H., Hauser, O., Rahman, H., & Zhang, D. (2026b). Call for science: AI-enabled frontiers in organizational science [Special issue call]. *Organization Science*.

Israeli, A., Kremiansky, A., & Tsur, O. (2022). This must be the place: Predicting engagement of online communities in a large-scale distributed campaign. In *Proceedings of the ACM Web Conference 2022* (pp. 1673–1684). ACM.

Jemine, G. (2025). "It falls upon you to create a better place": Exploring ephemeral online communities under the lens of organisational configurations. *International Journal of Organizational Analysis*, 33(10), 3896–3909.

Kohler, R. E. (1994). *Lords of the fly: Drosophila genetics and the experimental life*. University of Chicago Press.

Lee, M. Y., & Edmondson, A. C. (2017). Self-managing organizations: Exploring the limits of less-hierarchical organizing. *Research in Organizational Behavior*, 37, 35–58.

Leonelli, S. (2016). *Data-centric biology: A philosophical study*. University of Chicago Press.

Leonelli, S., & Ankeny, R. A. (2013). What makes a model organism? *Endeavour*, 37(4), 209–212.

Lewin, A. Y. (1992). On learning from outliers. In F. Y. Phillips & J. J. Rousseau (Eds.), *Systems and management science by extremal methods* (pp. 11–17). Kluwer.

Lewin, A. Y., & Volberda, H. W. (1999). Prolegomena on coevolution: A framework for research on strategy and new organizational forms. *Organization Science*, 10(5), 519–534.

Machlup, F. (1967). Theories of the firm: Marginalist, behavioral, managerial. *American Economic Review*, 57(1), 1–33.

O'Mahony, S., & Ferraro, F. (2007). The emergence of governance in an open source community. *Academy of Management Journal*, 50(5), 1079–1106.

Pfeffer, J. (1993). Barriers to the advance of organizational science: Paradigm development as a dependent variable. *Academy of Management Review*, 18(4), 599–620.

Rappaz, J., Catasta, M., West, R., & Aberer, K. (2018). Latent structure in collaboration: The case of Reddit r/place. In *Proceedings of the International AAAI Conference on Web and Social Media*, 12(1).

Simon, H. A., & Chase, W. G. (1973). Skill in chess. *American Scientist*, 61(4), 394–403.

Simpson, B., Lee, M., & Ellis, D. (2017, April 13). How we built r/Place. Reddit Blog.
