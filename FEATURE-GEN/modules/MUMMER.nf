process MUMMER {
   label 'ultralow'
    container 'mblanche/mummer4:latest'

    input:
        tuple val(sample), file(fasta), file(ref)
    output:
        path("./mummer_${sample}"), emit: mummer_out
        tuple val(sample), file("./mummer_${sample}/out.report"), emit: report

    script:

    """
    dnadiff ${ref} ${fasta}
    mkdir mummer_${sample}
    mv out.* mummer_${sample}
    """
}