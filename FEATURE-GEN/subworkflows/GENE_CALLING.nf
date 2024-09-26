/*
A subworkflows for calling genes from test genomes and a reference genomes

*/

include { PROKKA as PROKKA } from '../modules/PROKKA.nf'


workflow GENE_CALLING {

    take:
        ch_genomes        //    channel: (sample, fasta)

    main:

        PROKKA(ch_genomes)

    emit:
        proteins = PROKKA.out.amino_acids
        summary = PROKKA.out.summary

}