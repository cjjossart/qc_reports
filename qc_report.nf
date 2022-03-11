process QC_REPORT {
    tag "$meta.id"
    label 'process_low'

    conda (params.enable_conda ? "bioconda::pandas=1.1.5" : null)
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/pandas:1.1.5' : 
        'quay.io/biocontainers/pandas:1.1.5' }"
        
    input:
    tuple val(meta), path(txt)
    //path reference

    output:
    tuple val(meta), path("output.txt"), emit: qc_stuff

    """
    python $projectDir/bin/qc_report_stats.py $txt > output.txt

    """
}