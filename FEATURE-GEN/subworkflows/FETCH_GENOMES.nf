/*
A subworkflows for calling genes from test genomes and a reference genomes

*/

include { FETCH_GENOME as FETCH_GENOME } from '../modules/FEATURE_GEN.nf'
include { GUNZIP as GUNZIP } from '../modules/GUNZIP.nf'
include { REMOVE_GUIDED as REMOVE_GUIDED } from '../modules/FEATURE_GEN.nf'


workflow FETCH_GENOMES {

    take:
        ch_input         //    channel: (sample, acc)

    main:

        FETCH_GENOME(ch_input)

        GUNZIP(FETCH_GENOME.out.genome)

        REMOVE_GUIDED(GUNZIP.out.decomp)

    emit:

        genome = REMOVE_GUIDED.out.denovo

}