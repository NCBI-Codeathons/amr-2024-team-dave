process MUMMER {
   label 'ultrashort'
    container 'mblanche/mummer4:latest'

    input:
        tuple val(sample), file(fasta), file(ref)
    output:
        path("./mummer_${sample}"), emit: amrfinder_results

    script:

    """
    dnadiff ${ref} ${fasta}
    mkdir mummer_${sample}
    mv out.* mummer_${sample}
    """
}