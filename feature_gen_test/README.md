### Feature Generation Worflow

> This is a quick pipeline framework that I put together to let us test different methods of generating different features with different methods. This pipeline is written in nextflow and uses docker/singularity containers to deploy software. Right now I only have configuration files for running on my clusters, but we can add configuration files for it to run locally or on just about any system. We could also later incorporate this tools into a different framework like python/snakemake.

Running the Pipeline

```bash
 nextflow run ./FEATURE-GEN/ -c {config file}
```

## SNPs

> SNP Results can be found in the output folder {project_name}/GENERATE_FEATURES/VARIANT_CALLING/MUMMER/mummer_{sample_name}/out.snps . Currently the project_name is First_FeatureGen_Test. This SNP data is generated using [Mummers](https://github.com/mummer4/mummer) dnadiff workflow. This workflow does much more than just align genomes and call snps and might be usefull for other features(?). To process the 4 test genomes it took less than 2 minutes.

## Gene Calling

> Prokka is used for gene calling of every test genome
