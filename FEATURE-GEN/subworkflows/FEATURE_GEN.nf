/*
A subworkflows for calling genes from test genomes and a reference genomes

*/

include { NUC_FEATURES as NUC_FEATURES } from '../modules/FEATURE_GEN.nf'
include { PRO_FEATURES as PRO_FEATURES } from '../modules/FEATURE_GEN.nf'
include { PROKKA_PARSE as PROKKA_PARSE } from '../modules/FEATURE_GEN.nf'



workflow FEATURE_GEN {

    take:
        ch_genomes        //    channel: (sample, fasta)
        ch_proteins       //    channel: (sample, fasta)
        ch_prokka_out     //    channel: (sample, file)

    main:

        NUC_FEATURES(ch_genomes)
        PRO_FEATURES(ch_proteins)
        PROKKA_PARSE(ch_prokka_out)

    //emit:
}