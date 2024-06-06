from betterschema import core, render


@core.schema
class io_k8s_api_admissionregistration_v1_AuditAnnotation:
    """AuditAnnotation describes how to produce an audit annotation for an API request."""

    """Dependencies: []"""
    key: str
    valueExpression: str


@core.schema
class io_k8s_api_admissionregistration_v1_ExpressionWarning:
    """ExpressionWarning is a warning information that targets a specific expression."""

    """Dependencies: []"""
    fieldRef: str
    warning: str


@core.schema
class io_k8s_api_admissionregistration_v1_MatchCondition:
    """MatchCondition represents a condition which must by fulfilled for a request to be sent to a webhook."""

    """Dependencies: []"""
    expression: str
    name: str


@core.schema
class io_k8s_api_admissionregistration_v1_NamedRuleWithOperations:
    """NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames."""

    """Dependencies: []"""
    apiGroups: core.optional[list[str]]
    apiVersions: core.optional[list[str]]
    operations: core.optional[list[str]]
    resourceNames: core.optional[list[str]]
    resources: core.optional[list[str]]
    scope: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1_ParamKind:
    """ParamKind is a tuple of Group Kind and Version."""

    """Dependencies: []"""
    apiVersion: core.optional[str]
    kind: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1_RuleWithOperations:
    """RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid."""

    """Dependencies: []"""
    apiGroups: core.optional[list[str]]
    apiVersions: core.optional[list[str]]
    operations: core.optional[list[str]]
    resources: core.optional[list[str]]
    scope: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1_ServiceReference:
    """ServiceReference holds a reference to Service.legacy.k8s.io"""

    """Dependencies: []"""
    name: str
    namespace: str
    path: core.optional[str]
    port: core.optional[int]


@core.schema
class io_k8s_api_admissionregistration_v1_TypeChecking:
    """TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy"""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.ExpressionWarning']"""
    expressionWarnings: core.optional[
        list[io_k8s_api_admissionregistration_v1_ExpressionWarning]
    ]


@core.schema
class io_k8s_api_admissionregistration_v1_Validation:
    """Validation specifies the CEL expression which is used to apply the validation."""

    """Dependencies: []"""
    expression: str
    message: core.optional[str]
    messageExpression: core.optional[str]
    reason: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1_Variable:
    """Variable is the definition of a variable that is used for composition. A variable is defined as a named expression."""

    """Dependencies: []"""
    expression: str
    name: str


@core.schema
class io_k8s_api_admissionregistration_v1_WebhookClientConfig:
    """WebhookClientConfig contains the information to make a TLS connection with the webhook"""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.ServiceReference']"""
    caBundle: core.optional[str]
    service: core.optional[io_k8s_api_admissionregistration_v1_ServiceReference]
    url: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_AuditAnnotation:
    """AuditAnnotation describes how to produce an audit annotation for an API request."""

    """Dependencies: []"""
    key: str
    valueExpression: str


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ExpressionWarning:
    """ExpressionWarning is a warning information that targets a specific expression."""

    """Dependencies: []"""
    fieldRef: str
    warning: str


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_MatchCondition:
    """N/A"""

    """Dependencies: []"""
    expression: str
    name: str


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_NamedRuleWithOperations:
    """NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames."""

    """Dependencies: []"""
    apiGroups: core.optional[list[str]]
    apiVersions: core.optional[list[str]]
    operations: core.optional[list[str]]
    resourceNames: core.optional[list[str]]
    resources: core.optional[list[str]]
    scope: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ParamKind:
    """ParamKind is a tuple of Group Kind and Version."""

    """Dependencies: []"""
    apiVersion: core.optional[str]
    kind: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_TypeChecking:
    """TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy"""

    """Dependencies: ['io.k8s.api.admissionregistration.v1alpha1.ExpressionWarning']"""
    expressionWarnings: core.optional[
        list[io_k8s_api_admissionregistration_v1alpha1_ExpressionWarning]
    ]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_Validation:
    """Validation specifies the CEL expression which is used to apply the validation."""

    """Dependencies: []"""
    expression: str
    message: core.optional[str]
    messageExpression: core.optional[str]
    reason: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_Variable:
    """Variable is the definition of a variable that is used for composition."""

    """Dependencies: []"""
    expression: str
    name: str


@core.schema
class io_k8s_api_admissionregistration_v1beta1_AuditAnnotation:
    """AuditAnnotation describes how to produce an audit annotation for an API request."""

    """Dependencies: []"""
    key: str
    valueExpression: str


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ExpressionWarning:
    """ExpressionWarning is a warning information that targets a specific expression."""

    """Dependencies: []"""
    fieldRef: str
    warning: str


@core.schema
class io_k8s_api_admissionregistration_v1beta1_MatchCondition:
    """MatchCondition represents a condition which must be fulfilled for a request to be sent to a webhook."""

    """Dependencies: []"""
    expression: str
    name: str


@core.schema
class io_k8s_api_admissionregistration_v1beta1_NamedRuleWithOperations:
    """NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames."""

    """Dependencies: []"""
    apiGroups: core.optional[list[str]]
    apiVersions: core.optional[list[str]]
    operations: core.optional[list[str]]
    resourceNames: core.optional[list[str]]
    resources: core.optional[list[str]]
    scope: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ParamKind:
    """ParamKind is a tuple of Group Kind and Version."""

    """Dependencies: []"""
    apiVersion: core.optional[str]
    kind: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_TypeChecking:
    """TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy"""

    """Dependencies: ['io.k8s.api.admissionregistration.v1beta1.ExpressionWarning']"""
    expressionWarnings: core.optional[
        list[io_k8s_api_admissionregistration_v1beta1_ExpressionWarning]
    ]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_Validation:
    """Validation specifies the CEL expression which is used to apply the validation."""

    """Dependencies: []"""
    expression: str
    message: core.optional[str]
    messageExpression: core.optional[str]
    reason: core.optional[str]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_Variable:
    """Variable is the definition of a variable that is used for composition. A variable is defined as a named expression."""

    """Dependencies: []"""
    expression: str
    name: str


@core.schema
class io_k8s_api_apiserverinternal_v1alpha1_ServerStorageVersion:
    """An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend."""

    """Dependencies: []"""
    apiServerID: core.optional[str]
    decodableVersions: core.optional[list[str]]
    encodingVersion: core.optional[str]
    servedVersions: core.optional[list[str]]


@core.schema
class io_k8s_api_apiserverinternal_v1alpha1_StorageVersionSpec:
    """StorageVersionSpec is an empty spec."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_api_apps_v1_StatefulSetOrdinals:
    """StatefulSetOrdinals describes the policy used for replica ordinal assignment in this StatefulSet."""

    """Dependencies: []"""
    start: core.optional[int]


@core.schema
class io_k8s_api_apps_v1_StatefulSetPersistentVolumeClaimRetentionPolicy:
    """StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the StatefulSet VolumeClaimTemplates."""

    """Dependencies: []"""
    whenDeleted: core.optional[str]
    whenScaled: core.optional[str]


@core.schema
class io_k8s_api_authentication_v1_BoundObjectReference:
    """BoundObjectReference is a reference to an object that a token is bound to."""

    """Dependencies: []"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    name: core.optional[str]
    uid: core.optional[str]


@core.schema
class io_k8s_api_authentication_v1_TokenRequestSpec:
    """TokenRequestSpec contains client provided parameters of a token request."""

    """Dependencies: ['io.k8s.api.authentication.v1.BoundObjectReference']"""
    audiences: list[str]
    boundObjectRef: core.optional[io_k8s_api_authentication_v1_BoundObjectReference]
    expirationSeconds: core.optional[int]


@core.schema
class io_k8s_api_authentication_v1_TokenReviewSpec:
    """TokenReviewSpec is a description of the token authentication request."""

    """Dependencies: []"""
    audiences: core.optional[list[str]]
    token: core.optional[str]


@core.schema
class io_k8s_api_authentication_v1_UserInfo:
    """UserInfo holds the information about the user needed to implement the user.Info interface."""

    """Dependencies: []"""
    extra: core.optional[dict[str, str]]
    groups: core.optional[list[str]]
    uid: core.optional[str]
    username: core.optional[str]


@core.schema
class io_k8s_api_authentication_v1alpha1_SelfSubjectReviewStatus:
    """SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user."""

    """Dependencies: ['io.k8s.api.authentication.v1.UserInfo']"""
    userInfo: core.optional[io_k8s_api_authentication_v1_UserInfo]


@core.schema
class io_k8s_api_authentication_v1beta1_SelfSubjectReviewStatus:
    """SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user."""

    """Dependencies: ['io.k8s.api.authentication.v1.UserInfo']"""
    userInfo: core.optional[io_k8s_api_authentication_v1_UserInfo]


@core.schema
class io_k8s_api_authorization_v1_NonResourceAttributes:
    """NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface"""

    """Dependencies: []"""
    path: core.optional[str]
    verb: core.optional[str]


@core.schema
class io_k8s_api_authorization_v1_NonResourceRule:
    """NonResourceRule holds information that describes a rule for the non-resource"""

    """Dependencies: []"""
    nonResourceURLs: core.optional[list[str]]
    verbs: list[str]


@core.schema
class io_k8s_api_authorization_v1_ResourceAttributes:
    """ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface"""

    """Dependencies: []"""
    group: core.optional[str]
    name: core.optional[str]
    namespace: core.optional[str]
    resource: core.optional[str]
    subresource: core.optional[str]
    verb: core.optional[str]
    version: core.optional[str]


@core.schema
class io_k8s_api_authorization_v1_ResourceRule:
    """ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete."""

    """Dependencies: []"""
    apiGroups: core.optional[list[str]]
    resourceNames: core.optional[list[str]]
    resources: core.optional[list[str]]
    verbs: list[str]


@core.schema
class io_k8s_api_authorization_v1_SelfSubjectAccessReviewSpec:
    """SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set"""

    """Dependencies: ['io.k8s.api.authorization.v1.NonResourceAttributes', 'io.k8s.api.authorization.v1.ResourceAttributes']"""
    nonResourceAttributes: core.optional[
        io_k8s_api_authorization_v1_NonResourceAttributes
    ]
    resourceAttributes: core.optional[io_k8s_api_authorization_v1_ResourceAttributes]


@core.schema
class io_k8s_api_authorization_v1_SelfSubjectRulesReviewSpec:
    """SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview."""

    """Dependencies: []"""
    namespace: core.optional[str]


@core.schema
class io_k8s_api_authorization_v1_SubjectAccessReviewSpec:
    """SubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set"""

    """Dependencies: ['io.k8s.api.authorization.v1.NonResourceAttributes', 'io.k8s.api.authorization.v1.ResourceAttributes']"""
    extra: core.optional[dict[str, str]]
    groups: core.optional[list[str]]
    nonResourceAttributes: core.optional[
        io_k8s_api_authorization_v1_NonResourceAttributes
    ]
    resourceAttributes: core.optional[io_k8s_api_authorization_v1_ResourceAttributes]
    uid: core.optional[str]
    user: core.optional[str]


@core.schema
class io_k8s_api_authorization_v1_SubjectAccessReviewStatus:
    """SubjectAccessReviewStatus"""

    """Dependencies: []"""
    allowed: bool
    denied: core.optional[bool]
    evaluationError: core.optional[str]
    reason: core.optional[str]


@core.schema
class io_k8s_api_authorization_v1_SubjectRulesReviewStatus:
    """SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete."""

    """Dependencies: ['io.k8s.api.authorization.v1.NonResourceRule', 'io.k8s.api.authorization.v1.ResourceRule']"""
    evaluationError: core.optional[str]
    incomplete: bool
    nonResourceRules: list[io_k8s_api_authorization_v1_NonResourceRule]
    resourceRules: list[io_k8s_api_authorization_v1_ResourceRule]


@core.schema
class io_k8s_api_autoscaling_v1_CrossVersionObjectReference:
    """CrossVersionObjectReference contains enough information to let you identify the referred resource."""

    """Dependencies: []"""
    apiVersion: core.optional[str]
    kind: str
    name: str


@core.schema
class io_k8s_api_autoscaling_v1_HorizontalPodAutoscalerSpec:
    """specification of a horizontal pod autoscaler."""

    """Dependencies: ['io.k8s.api.autoscaling.v1.CrossVersionObjectReference']"""
    maxReplicas: int
    minReplicas: core.optional[int]
    scaleTargetRef: io_k8s_api_autoscaling_v1_CrossVersionObjectReference
    targetCPUUtilizationPercentage: core.optional[int]


@core.schema
class io_k8s_api_autoscaling_v1_ScaleSpec:
    """ScaleSpec describes the attributes of a scale subresource."""

    """Dependencies: []"""
    replicas: core.optional[int]


@core.schema
class io_k8s_api_autoscaling_v1_ScaleStatus:
    """ScaleStatus represents the current status of a scale subresource."""

    """Dependencies: []"""
    replicas: int
    selector: core.optional[str]


@core.schema
class io_k8s_api_autoscaling_v2_CrossVersionObjectReference:
    """CrossVersionObjectReference contains enough information to let you identify the referred resource."""

    """Dependencies: []"""
    apiVersion: core.optional[str]
    kind: str
    name: str


@core.schema
class io_k8s_api_autoscaling_v2_HPAScalingPolicy:
    """HPAScalingPolicy is a single policy which must hold true for a specified past interval."""

    """Dependencies: []"""
    periodSeconds: int
    type: str
    value: int


@core.schema
class io_k8s_api_autoscaling_v2_HPAScalingRules:
    """HPAScalingRules configures the scaling behavior for one direction. These Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.HPAScalingPolicy']"""
    policies: core.optional[list[io_k8s_api_autoscaling_v2_HPAScalingPolicy]]
    selectPolicy: core.optional[str]
    stabilizationWindowSeconds: core.optional[int]


@core.schema
class io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerBehavior:
    """HorizontalPodAutoscalerBehavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively)."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.HPAScalingRules', 'io.k8s.api.autoscaling.v2.HPAScalingRules']"""
    scaleDown: core.optional[io_k8s_api_autoscaling_v2_HPAScalingRules]
    scaleUp: core.optional[io_k8s_api_autoscaling_v2_HPAScalingRules]


@core.schema
class io_k8s_api_batch_v1_PodFailurePolicyOnExitCodesRequirement:
    """PodFailurePolicyOnExitCodesRequirement describes the requirement for handling a failed pod based on its container exit codes. In particular, it lookups the .state.terminated.exitCode for each app container and init container status, represented by the .status.containerStatuses and .status.initContainerStatuses fields in the Pod status, respectively. Containers completed with success (exit code 0) are excluded from the requirement check."""

    """Dependencies: []"""
    containerName: core.optional[str]
    operator: str
    values: list[int]


@core.schema
class io_k8s_api_batch_v1_PodFailurePolicyOnPodConditionsPattern:
    """PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type."""

    """Dependencies: []"""
    status: str
    type: str


@core.schema
class io_k8s_api_batch_v1_PodFailurePolicyRule:
    """PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of onExitCodes and onPodConditions, but not both, can be used in each rule."""

    """Dependencies: ['io.k8s.api.batch.v1.PodFailurePolicyOnExitCodesRequirement', 'io.k8s.api.batch.v1.PodFailurePolicyOnPodConditionsPattern']"""
    action: str
    onExitCodes: core.optional[
        io_k8s_api_batch_v1_PodFailurePolicyOnExitCodesRequirement
    ]
    onPodConditions: core.optional[
        list[io_k8s_api_batch_v1_PodFailurePolicyOnPodConditionsPattern]
    ]


@core.schema
class io_k8s_api_batch_v1_SuccessPolicyRule:
    """SuccessPolicyRule describes rule for declaring a Job as succeeded. Each rule must have at least one of the "succeededIndexes" or "succeededCount" specified."""

    """Dependencies: []"""
    succeededCount: core.optional[int]
    succeededIndexes: core.optional[str]


@core.schema
class io_k8s_api_batch_v1_UncountedTerminatedPods:
    """UncountedTerminatedPods holds UIDs of Pods that have terminated but haven't been accounted in Job status counters."""

    """Dependencies: []"""
    failed: core.optional[list[str]]
    succeeded: core.optional[list[str]]


@core.schema
class io_k8s_api_certificates_v1_CertificateSigningRequestSpec:
    """CertificateSigningRequestSpec contains the certificate request."""

    """Dependencies: []"""
    expirationSeconds: core.optional[int]
    extra: core.optional[dict[str, str]]
    groups: core.optional[list[str]]
    request: str
    signerName: str
    uid: core.optional[str]
    usages: core.optional[list[str]]
    username: core.optional[str]


@core.schema
class io_k8s_api_certificates_v1alpha1_ClusterTrustBundleSpec:
    """ClusterTrustBundleSpec contains the signer and trust anchors."""

    """Dependencies: []"""
    signerName: core.optional[str]
    trustBundle: str


@core.schema
class io_k8s_api_core_v1_AWSElasticBlockStoreVolumeSource:
    """Represents a Persistent Disk resource in AWS.

    An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.
    """

    """Dependencies: []"""
    fsType: core.optional[str]
    partition: core.optional[int]
    readOnly: core.optional[bool]
    volumeID: str


@core.schema
class io_k8s_api_core_v1_AppArmorProfile:
    """AppArmorProfile defines a pod or container's AppArmor settings."""

    """Dependencies: []"""
    localhostProfile: core.optional[str]
    type: str


@core.schema
class io_k8s_api_core_v1_AttachedVolume:
    """AttachedVolume describes a volume attached to a node"""

    """Dependencies: []"""
    devicePath: str
    name: str


@core.schema
class io_k8s_api_core_v1_AzureDiskVolumeSource:
    """AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod."""

    """Dependencies: []"""
    cachingMode: core.optional[str]
    diskName: str
    diskURI: str
    fsType: core.optional[str]
    kind: core.optional[str]
    readOnly: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_AzureFilePersistentVolumeSource:
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod."""

    """Dependencies: []"""
    readOnly: core.optional[bool]
    secretName: str
    secretNamespace: core.optional[str]
    shareName: str


@core.schema
class io_k8s_api_core_v1_AzureFileVolumeSource:
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod."""

    """Dependencies: []"""
    readOnly: core.optional[bool]
    secretName: str
    shareName: str


@core.schema
class io_k8s_api_core_v1_Capabilities:
    """Adds and removes POSIX capabilities from running containers."""

    """Dependencies: []"""
    add: core.optional[list[str]]
    drop: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_ClaimSource:
    """ClaimSource describes a reference to a ResourceClaim.

    Exactly one of these fields should be set.  Consumers of this type must treat an empty object as if it has an unknown value.
    """

    """Dependencies: []"""
    resourceClaimName: core.optional[str]
    resourceClaimTemplateName: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ClientIPConfig:
    """ClientIPConfig represents the configurations of Client IP based session affinity."""

    """Dependencies: []"""
    timeoutSeconds: core.optional[int]


@core.schema
class io_k8s_api_core_v1_ComponentCondition:
    """Information about the condition of a component."""

    """Dependencies: []"""
    error: core.optional[str]
    message: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_core_v1_ConfigMapEnvSource:
    """ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

    The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.
    """

    """Dependencies: []"""
    name: core.optional[str]
    optional: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_ConfigMapKeySelector:
    """Selects a key from a ConfigMap."""

    """Dependencies: []"""
    key: str
    name: core.optional[str]
    optional: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_ConfigMapNodeConfigSource:
    """ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration"""

    """Dependencies: []"""
    kubeletConfigKey: str
    name: str
    namespace: str
    resourceVersion: core.optional[str]
    uid: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ContainerImage:
    """Describe a container image"""

    """Dependencies: []"""
    names: core.optional[list[str]]
    sizeBytes: core.optional[int]


@core.schema
class io_k8s_api_core_v1_ContainerPort:
    """ContainerPort represents a network port in a single container."""

    """Dependencies: []"""
    containerPort: int
    hostIP: core.optional[str]
    hostPort: core.optional[int]
    name: core.optional[str]
    protocol: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ContainerResizePolicy:
    """ContainerResizePolicy represents resource resize policy for the container."""

    """Dependencies: []"""
    resourceName: str
    restartPolicy: str


@core.schema
class io_k8s_api_core_v1_ContainerStateWaiting:
    """ContainerStateWaiting is a waiting state of a container."""

    """Dependencies: []"""
    message: core.optional[str]
    reason: core.optional[str]


@core.schema
class io_k8s_api_core_v1_DaemonEndpoint:
    """DaemonEndpoint contains information about a single Daemon endpoint."""

    """Dependencies: []"""
    Port: int


@core.schema
class io_k8s_api_core_v1_EndpointPort:
    """EndpointPort is a tuple that describes a single port."""

    """Dependencies: []"""
    appProtocol: core.optional[str]
    name: core.optional[str]
    port: int
    protocol: core.optional[str]


@core.schema
class io_k8s_api_core_v1_EventSource:
    """EventSource contains information for an event."""

    """Dependencies: []"""
    component: core.optional[str]
    host: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ExecAction:
    """ExecAction describes a "run in container" action."""

    """Dependencies: []"""
    command: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_FCVolumeSource:
    """Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling."""

    """Dependencies: []"""
    fsType: core.optional[str]
    lun: core.optional[int]
    readOnly: core.optional[bool]
    targetWWNs: core.optional[list[str]]
    wwids: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_FlockerVolumeSource:
    """Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling."""

    """Dependencies: []"""
    datasetName: core.optional[str]
    datasetUUID: core.optional[str]


@core.schema
class io_k8s_api_core_v1_GCEPersistentDiskVolumeSource:
    """Represents a Persistent Disk resource in Google Compute Engine.

    A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.
    """

    """Dependencies: []"""
    fsType: core.optional[str]
    partition: core.optional[int]
    pdName: str
    readOnly: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_GRPCAction:
    """N/A"""

    """Dependencies: []"""
    port: int
    service: core.optional[str]


@core.schema
class io_k8s_api_core_v1_GitRepoVolumeSource:
    """Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.

    DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    """

    """Dependencies: []"""
    directory: core.optional[str]
    repository: str
    revision: core.optional[str]


@core.schema
class io_k8s_api_core_v1_GlusterfsPersistentVolumeSource:
    """Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling."""

    """Dependencies: []"""
    endpoints: str
    endpointsNamespace: core.optional[str]
    path: str
    readOnly: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_GlusterfsVolumeSource:
    """Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling."""

    """Dependencies: []"""
    endpoints: str
    path: str
    readOnly: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_HTTPHeader:
    """HTTPHeader describes a custom header to be used in HTTP probes"""

    """Dependencies: []"""
    name: str
    value: str


@core.schema
class io_k8s_api_core_v1_HostAlias:
    """HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file."""

    """Dependencies: []"""
    hostnames: core.optional[list[str]]
    ip: str


@core.schema
class io_k8s_api_core_v1_HostIP:
    """HostIP represents a single IP address allocated to the host."""

    """Dependencies: []"""
    ip: core.optional[str]


@core.schema
class io_k8s_api_core_v1_HostPathVolumeSource:
    """Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling."""

    """Dependencies: []"""
    path: str
    type: core.optional[str]


@core.schema
class io_k8s_api_core_v1_KeyToPath:
    """Maps a string key to a path within a volume."""

    """Dependencies: []"""
    key: str
    mode: core.optional[int]
    path: str


@core.schema
class io_k8s_api_core_v1_LimitRangeItem:
    """LimitRangeItem defines a min/max usage limit for any resource that matches on kind."""

    """Dependencies: []"""
    default: core.optional[dict[str, str]]
    defaultRequest: core.optional[dict[str, str]]
    max: core.optional[dict[str, str]]
    maxLimitRequestRatio: core.optional[dict[str, str]]
    min: core.optional[dict[str, str]]
    type: str


@core.schema
class io_k8s_api_core_v1_LimitRangeSpec:
    """LimitRangeSpec defines a min/max usage limit for resources that match on kind."""

    """Dependencies: ['io.k8s.api.core.v1.LimitRangeItem']"""
    limits: list[io_k8s_api_core_v1_LimitRangeItem]


@core.schema
class io_k8s_api_core_v1_LinuxContainerUser:
    """LinuxContainerUser represents user identity information in Linux containers"""

    """Dependencies: []"""
    gid: int
    supplementalGroups: core.optional[list[int]]
    uid: int


@core.schema
class io_k8s_api_core_v1_LocalObjectReference:
    """LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace."""

    """Dependencies: []"""
    name: core.optional[str]


@core.schema
class io_k8s_api_core_v1_LocalVolumeSource:
    """Local represents directly-attached storage with node affinity (Beta feature)"""

    """Dependencies: []"""
    fsType: core.optional[str]
    path: str


@core.schema
class io_k8s_api_core_v1_ModifyVolumeStatus:
    """ModifyVolumeStatus represents the status object of ControllerModifyVolume operation"""

    """Dependencies: []"""
    status: str
    targetVolumeAttributesClassName: core.optional[str]


@core.schema
class io_k8s_api_core_v1_NFSVolumeSource:
    """Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling."""

    """Dependencies: []"""
    path: str
    readOnly: core.optional[bool]
    server: str


@core.schema
class io_k8s_api_core_v1_NamespaceSpec:
    """NamespaceSpec describes the attributes on a Namespace."""

    """Dependencies: []"""
    finalizers: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_NodeAddress:
    """NodeAddress contains information for the node's address."""

    """Dependencies: []"""
    address: str
    type: str


@core.schema
class io_k8s_api_core_v1_NodeConfigSource:
    """NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22"""

    """Dependencies: ['io.k8s.api.core.v1.ConfigMapNodeConfigSource']"""
    configMap: core.optional[io_k8s_api_core_v1_ConfigMapNodeConfigSource]


@core.schema
class io_k8s_api_core_v1_NodeConfigStatus:
    """NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource."""

    """Dependencies: ['io.k8s.api.core.v1.NodeConfigSource', 'io.k8s.api.core.v1.NodeConfigSource', 'io.k8s.api.core.v1.NodeConfigSource']"""
    active: core.optional[io_k8s_api_core_v1_NodeConfigSource]
    assigned: core.optional[io_k8s_api_core_v1_NodeConfigSource]
    error: core.optional[str]
    lastKnownGood: core.optional[io_k8s_api_core_v1_NodeConfigSource]


@core.schema
class io_k8s_api_core_v1_NodeDaemonEndpoints:
    """NodeDaemonEndpoints lists ports opened by daemons running on the Node."""

    """Dependencies: ['io.k8s.api.core.v1.DaemonEndpoint']"""
    kubeletEndpoint: core.optional[io_k8s_api_core_v1_DaemonEndpoint]


@core.schema
class io_k8s_api_core_v1_NodeRuntimeHandlerFeatures:
    """NodeRuntimeHandlerFeatures is a set of runtime features."""

    """Dependencies: []"""
    recursiveReadOnlyMounts: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_NodeSelectorRequirement:
    """A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values."""

    """Dependencies: []"""
    key: str
    operator: str
    values: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_NodeSelectorTerm:
    """A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm."""

    """Dependencies: ['io.k8s.api.core.v1.NodeSelectorRequirement', 'io.k8s.api.core.v1.NodeSelectorRequirement']"""
    matchExpressions: core.optional[list[io_k8s_api_core_v1_NodeSelectorRequirement]]
    matchFields: core.optional[list[io_k8s_api_core_v1_NodeSelectorRequirement]]


@core.schema
class io_k8s_api_core_v1_NodeSystemInfo:
    """NodeSystemInfo is a set of ids/uuids to uniquely identify the node."""

    """Dependencies: []"""
    architecture: str
    bootID: str
    containerRuntimeVersion: str
    kernelVersion: str
    kubeProxyVersion: str
    kubeletVersion: str
    machineID: str
    operatingSystem: str
    osImage: str
    systemUUID: str


@core.schema
class io_k8s_api_core_v1_ObjectFieldSelector:
    """ObjectFieldSelector selects an APIVersioned field of an object."""

    """Dependencies: []"""
    apiVersion: core.optional[str]
    fieldPath: str


@core.schema
class io_k8s_api_core_v1_ObjectReference:
    """ObjectReference contains enough information to let you inspect or modify the referred object."""

    """Dependencies: []"""
    apiVersion: core.optional[str]
    fieldPath: core.optional[str]
    kind: core.optional[str]
    name: core.optional[str]
    namespace: core.optional[str]
    resourceVersion: core.optional[str]
    uid: core.optional[str]


@core.schema
class io_k8s_api_core_v1_PersistentVolumeClaimVolumeSource:
    """PersistentVolumeClaimVolumeSource references the user's PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system)."""

    """Dependencies: []"""
    claimName: str
    readOnly: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_PhotonPersistentDiskVolumeSource:
    """Represents a Photon Controller persistent disk resource."""

    """Dependencies: []"""
    fsType: core.optional[str]
    pdID: str


@core.schema
class io_k8s_api_core_v1_PodDNSConfigOption:
    """PodDNSConfigOption defines DNS resolver options of a pod."""

    """Dependencies: []"""
    name: core.optional[str]
    value: core.optional[str]


@core.schema
class io_k8s_api_core_v1_PodIP:
    """PodIP represents a single IP address allocated to the pod."""

    """Dependencies: []"""
    ip: core.optional[str]


@core.schema
class io_k8s_api_core_v1_PodOS:
    """PodOS defines the OS parameters of a pod."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_core_v1_PodReadinessGate:
    """PodReadinessGate contains the reference to a pod condition"""

    """Dependencies: []"""
    conditionType: str


@core.schema
class io_k8s_api_core_v1_PodResourceClaim:
    """PodResourceClaim references exactly one ResourceClaim through a ClaimSource. It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name."""

    """Dependencies: ['io.k8s.api.core.v1.ClaimSource']"""
    name: str
    source: core.optional[io_k8s_api_core_v1_ClaimSource]


@core.schema
class io_k8s_api_core_v1_PodResourceClaimStatus:
    """PodResourceClaimStatus is stored in the PodStatus for each PodResourceClaim which references a ResourceClaimTemplate. It stores the generated name for the corresponding ResourceClaim."""

    """Dependencies: []"""
    name: str
    resourceClaimName: core.optional[str]


@core.schema
class io_k8s_api_core_v1_PodSchedulingGate:
    """PodSchedulingGate is associated to a Pod to guard its scheduling."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_core_v1_PortStatus:
    """N/A"""

    """Dependencies: []"""
    error: core.optional[str]
    port: int
    protocol: str


@core.schema
class io_k8s_api_core_v1_PortworxVolumeSource:
    """PortworxVolumeSource represents a Portworx volume resource."""

    """Dependencies: []"""
    fsType: core.optional[str]
    readOnly: core.optional[bool]
    volumeID: str


@core.schema
class io_k8s_api_core_v1_PreferredSchedulingTerm:
    """An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op)."""

    """Dependencies: ['io.k8s.api.core.v1.NodeSelectorTerm']"""
    preference: io_k8s_api_core_v1_NodeSelectorTerm
    weight: int


@core.schema
class io_k8s_api_core_v1_QuobyteVolumeSource:
    """Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling."""

    """Dependencies: []"""
    group: core.optional[str]
    readOnly: core.optional[bool]
    registry: str
    tenant: core.optional[str]
    user: core.optional[str]
    volume: str


@core.schema
class io_k8s_api_core_v1_RBDVolumeSource:
    """Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference']"""
    fsType: core.optional[str]
    image: str
    keyring: core.optional[str]
    monitors: list[str]
    pool: core.optional[str]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_LocalObjectReference]
    user: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ResourceClaim:
    """ResourceClaim references one entry in PodSpec.ResourceClaims."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_core_v1_ResourceQuotaStatus:
    """ResourceQuotaStatus defines the enforced hard limits and observed use."""

    """Dependencies: []"""
    hard: core.optional[dict[str, str]]
    used: core.optional[dict[str, str]]


@core.schema
class io_k8s_api_core_v1_ResourceRequirements:
    """ResourceRequirements describes the compute resource requirements."""

    """Dependencies: ['io.k8s.api.core.v1.ResourceClaim']"""
    claims: core.optional[list[io_k8s_api_core_v1_ResourceClaim]]
    limits: core.optional[dict[str, str]]
    requests: core.optional[dict[str, str]]


@core.schema
class io_k8s_api_core_v1_SELinuxOptions:
    """SELinuxOptions are the labels to be applied to the container"""

    """Dependencies: []"""
    level: core.optional[str]
    role: core.optional[str]
    type: core.optional[str]
    user: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ScaleIOVolumeSource:
    """ScaleIOVolumeSource represents a persistent ScaleIO volume"""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference']"""
    fsType: core.optional[str]
    gateway: str
    protectionDomain: core.optional[str]
    readOnly: core.optional[bool]
    secretRef: io_k8s_api_core_v1_LocalObjectReference
    sslEnabled: core.optional[bool]
    storageMode: core.optional[str]
    storagePool: core.optional[str]
    system: str
    volumeName: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ScopedResourceSelectorRequirement:
    """A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values."""

    """Dependencies: []"""
    operator: str
    scopeName: str
    values: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_SeccompProfile:
    """SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set."""

    """Dependencies: []"""
    localhostProfile: core.optional[str]
    type: str


@core.schema
class io_k8s_api_core_v1_SecretEnvSource:
    """SecretEnvSource selects a Secret to populate the environment variables with.

    The contents of the target Secret's Data field will represent the key-value pairs as environment variables.
    """

    """Dependencies: []"""
    name: core.optional[str]
    optional: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_SecretKeySelector:
    """SecretKeySelector selects a key of a Secret."""

    """Dependencies: []"""
    key: str
    name: core.optional[str]
    optional: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_SecretProjection:
    """Adapts a secret into a projected volume.

    The contents of the target Secret's Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.
    """

    """Dependencies: ['io.k8s.api.core.v1.KeyToPath']"""
    items: core.optional[list[io_k8s_api_core_v1_KeyToPath]]
    name: core.optional[str]
    optional: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_SecretReference:
    """SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace"""

    """Dependencies: []"""
    name: core.optional[str]
    namespace: core.optional[str]


@core.schema
class io_k8s_api_core_v1_SecretVolumeSource:
    """Adapts a Secret into a volume.

    The contents of the target Secret's Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.
    """

    """Dependencies: ['io.k8s.api.core.v1.KeyToPath']"""
    defaultMode: core.optional[int]
    items: core.optional[list[io_k8s_api_core_v1_KeyToPath]]
    optional: core.optional[bool]
    secretName: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ServiceAccountTokenProjection:
    """ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise)."""

    """Dependencies: []"""
    audience: core.optional[str]
    expirationSeconds: core.optional[int]
    path: str


@core.schema
class io_k8s_api_core_v1_SessionAffinityConfig:
    """SessionAffinityConfig represents the configurations of session affinity."""

    """Dependencies: ['io.k8s.api.core.v1.ClientIPConfig']"""
    clientIP: core.optional[io_k8s_api_core_v1_ClientIPConfig]


@core.schema
class io_k8s_api_core_v1_SleepAction:
    """SleepAction describes a "sleep" action."""

    """Dependencies: []"""
    seconds: int


@core.schema
class io_k8s_api_core_v1_StorageOSPersistentVolumeSource:
    """Represents a StorageOS persistent volume resource."""

    """Dependencies: ['io.k8s.api.core.v1.ObjectReference']"""
    fsType: core.optional[str]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_ObjectReference]
    volumeName: core.optional[str]
    volumeNamespace: core.optional[str]


@core.schema
class io_k8s_api_core_v1_StorageOSVolumeSource:
    """Represents a StorageOS persistent volume resource."""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference']"""
    fsType: core.optional[str]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_LocalObjectReference]
    volumeName: core.optional[str]
    volumeNamespace: core.optional[str]


@core.schema
class io_k8s_api_core_v1_Sysctl:
    """Sysctl defines a kernel parameter to be set"""

    """Dependencies: []"""
    name: str
    value: str


@core.schema
class io_k8s_api_core_v1_Toleration:
    """The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>."""

    """Dependencies: []"""
    effect: core.optional[str]
    key: core.optional[str]
    operator: core.optional[str]
    tolerationSeconds: core.optional[int]
    value: core.optional[str]


@core.schema
class io_k8s_api_core_v1_TopologySelectorLabelRequirement:
    """A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future."""

    """Dependencies: []"""
    key: str
    values: list[str]


@core.schema
class io_k8s_api_core_v1_TopologySelectorTerm:
    """A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future."""

    """Dependencies: ['io.k8s.api.core.v1.TopologySelectorLabelRequirement']"""
    matchLabelExpressions: core.optional[
        list[io_k8s_api_core_v1_TopologySelectorLabelRequirement]
    ]


@core.schema
class io_k8s_api_core_v1_TypedLocalObjectReference:
    """TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace."""

    """Dependencies: []"""
    apiGroup: core.optional[str]
    kind: str
    name: str


@core.schema
class io_k8s_api_core_v1_TypedObjectReference:
    """N/A"""

    """Dependencies: []"""
    apiGroup: core.optional[str]
    kind: str
    name: str
    namespace: core.optional[str]


@core.schema
class io_k8s_api_core_v1_VolumeDevice:
    """volumeDevice describes a mapping of a raw block device within a container."""

    """Dependencies: []"""
    devicePath: str
    name: str


@core.schema
class io_k8s_api_core_v1_VolumeMount:
    """VolumeMount describes a mounting of a Volume within a container."""

    """Dependencies: []"""
    mountPath: str
    mountPropagation: core.optional[str]
    name: str
    readOnly: core.optional[bool]
    recursiveReadOnly: core.optional[str]
    subPath: core.optional[str]
    subPathExpr: core.optional[str]


@core.schema
class io_k8s_api_core_v1_VolumeMountStatus:
    """VolumeMountStatus shows status of volume mounts."""

    """Dependencies: []"""
    mountPath: str
    name: str
    readOnly: core.optional[bool]
    recursiveReadOnly: core.optional[str]


@core.schema
class io_k8s_api_core_v1_VolumeResourceRequirements:
    """VolumeResourceRequirements describes the storage resource requirements for a volume."""

    """Dependencies: []"""
    limits: core.optional[dict[str, str]]
    requests: core.optional[dict[str, str]]


@core.schema
class io_k8s_api_core_v1_VsphereVirtualDiskVolumeSource:
    """Represents a vSphere volume resource."""

    """Dependencies: []"""
    fsType: core.optional[str]
    storagePolicyID: core.optional[str]
    storagePolicyName: core.optional[str]
    volumePath: str


@core.schema
class io_k8s_api_core_v1_WindowsSecurityContextOptions:
    """WindowsSecurityContextOptions contain Windows-specific options and credentials."""

    """Dependencies: []"""
    gmsaCredentialSpec: core.optional[str]
    gmsaCredentialSpecName: core.optional[str]
    hostProcess: core.optional[bool]
    runAsUserName: core.optional[str]


@core.schema
class io_k8s_api_discovery_v1_EndpointConditions:
    """EndpointConditions represents the current condition of an endpoint."""

    """Dependencies: []"""
    ready: core.optional[bool]
    serving: core.optional[bool]
    terminating: core.optional[bool]


@core.schema
class io_k8s_api_discovery_v1_EndpointPort:
    """EndpointPort represents a Port used by an EndpointSlice"""

    """Dependencies: []"""
    appProtocol: core.optional[str]
    name: core.optional[str]
    port: core.optional[int]
    protocol: core.optional[str]


@core.schema
class io_k8s_api_discovery_v1_ForZone:
    """ForZone provides information about which zones should consume this endpoint."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_flowcontrol_v1_ExemptPriorityLevelConfiguration:
    """ExemptPriorityLevelConfiguration describes the configurable aspects of the handling of exempt requests. In the mandatory exempt configuration object the values in the fields here can be modified by authorized users, unlike the rest of the `spec`."""

    """Dependencies: []"""
    lendablePercent: core.optional[int]
    nominalConcurrencyShares: core.optional[int]


@core.schema
class io_k8s_api_flowcontrol_v1_FlowDistinguisherMethod:
    """FlowDistinguisherMethod specifies the method of a flow distinguisher."""

    """Dependencies: []"""
    type: str


@core.schema
class io_k8s_api_flowcontrol_v1_GroupSubject:
    """GroupSubject holds detailed information for group-kind subject."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_flowcontrol_v1_NonResourcePolicyRule:
    """NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request."""

    """Dependencies: []"""
    nonResourceURLs: list[str]
    verbs: list[str]


@core.schema
class io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationReference:
    """PriorityLevelConfigurationReference contains information that points to the "request-priority" being used."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_flowcontrol_v1_QueuingConfiguration:
    """QueuingConfiguration holds the configuration parameters for queuing"""

    """Dependencies: []"""
    handSize: core.optional[int]
    queueLengthLimit: core.optional[int]
    queues: core.optional[int]


@core.schema
class io_k8s_api_flowcontrol_v1_ResourcePolicyRule:
    """ResourcePolicyRule is a predicate that matches some resource requests, testing the request's verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request's namespace."""

    """Dependencies: []"""
    apiGroups: list[str]
    clusterScope: core.optional[bool]
    namespaces: core.optional[list[str]]
    resources: list[str]
    verbs: list[str]


@core.schema
class io_k8s_api_flowcontrol_v1_ServiceAccountSubject:
    """ServiceAccountSubject holds detailed information for service-account-kind subject."""

    """Dependencies: []"""
    name: str
    namespace: str


@core.schema
class io_k8s_api_flowcontrol_v1_UserSubject:
    """UserSubject holds detailed information for user-kind subject."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_flowcontrol_v1beta3_ExemptPriorityLevelConfiguration:
    """ExemptPriorityLevelConfiguration describes the configurable aspects of the handling of exempt requests. In the mandatory exempt configuration object the values in the fields here can be modified by authorized users, unlike the rest of the `spec`."""

    """Dependencies: []"""
    lendablePercent: core.optional[int]
    nominalConcurrencyShares: core.optional[int]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_FlowDistinguisherMethod:
    """FlowDistinguisherMethod specifies the method of a flow distinguisher."""

    """Dependencies: []"""
    type: str


@core.schema
class io_k8s_api_flowcontrol_v1beta3_GroupSubject:
    """GroupSubject holds detailed information for group-kind subject."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_flowcontrol_v1beta3_NonResourcePolicyRule:
    """NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request."""

    """Dependencies: []"""
    nonResourceURLs: list[str]
    verbs: list[str]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationReference:
    """PriorityLevelConfigurationReference contains information that points to the "request-priority" being used."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_flowcontrol_v1beta3_QueuingConfiguration:
    """QueuingConfiguration holds the configuration parameters for queuing"""

    """Dependencies: []"""
    handSize: core.optional[int]
    queueLengthLimit: core.optional[int]
    queues: core.optional[int]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_ResourcePolicyRule:
    """ResourcePolicyRule is a predicate that matches some resource requests, testing the request's verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request's namespace."""

    """Dependencies: []"""
    apiGroups: list[str]
    clusterScope: core.optional[bool]
    namespaces: core.optional[list[str]]
    resources: list[str]
    verbs: list[str]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_ServiceAccountSubject:
    """ServiceAccountSubject holds detailed information for service-account-kind subject."""

    """Dependencies: []"""
    name: str
    namespace: str


@core.schema
class io_k8s_api_flowcontrol_v1beta3_UserSubject:
    """UserSubject holds detailed information for user-kind subject."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_networking_v1_IPBlock:
    """IPBlock describes a particular CIDR (Ex. "192.168.1.0/24","2001:db8::/64") that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The except entry describes CIDRs that should not be included within this rule."""

    """Dependencies: []"""
    cidr: str
    except_: core.optional[list[str]]


@core.schema
class io_k8s_api_networking_v1_IngressClassParametersReference:
    """IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource."""

    """Dependencies: []"""
    apiGroup: core.optional[str]
    kind: str
    name: str
    namespace: core.optional[str]
    scope: core.optional[str]


@core.schema
class io_k8s_api_networking_v1_IngressClassSpec:
    """IngressClassSpec provides information about the class of an Ingress."""

    """Dependencies: ['io.k8s.api.networking.v1.IngressClassParametersReference']"""
    controller: core.optional[str]
    parameters: core.optional[io_k8s_api_networking_v1_IngressClassParametersReference]


@core.schema
class io_k8s_api_networking_v1_IngressPortStatus:
    """IngressPortStatus represents the error condition of a service port"""

    """Dependencies: []"""
    error: core.optional[str]
    port: int
    protocol: str


@core.schema
class io_k8s_api_networking_v1_IngressTLS:
    """IngressTLS describes the transport layer security associated with an ingress."""

    """Dependencies: []"""
    hosts: core.optional[list[str]]
    secretName: core.optional[str]


@core.schema
class io_k8s_api_networking_v1_ServiceBackendPort:
    """ServiceBackendPort is the service port being referenced."""

    """Dependencies: []"""
    name: core.optional[str]
    number: core.optional[int]


@core.schema
class io_k8s_api_networking_v1alpha1_ParentReference:
    """ParentReference describes a reference to a parent object."""

    """Dependencies: []"""
    group: core.optional[str]
    name: str
    namespace: core.optional[str]
    resource: str


@core.schema
class io_k8s_api_networking_v1alpha1_ServiceCIDRSpec:
    """ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services."""

    """Dependencies: []"""
    cidrs: core.optional[list[str]]


@core.schema
class io_k8s_api_node_v1_Overhead:
    """Overhead structure represents the resource overhead associated with running a pod."""

    """Dependencies: []"""
    podFixed: core.optional[dict[str, str]]


@core.schema
class io_k8s_api_node_v1_Scheduling:
    """Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass."""

    """Dependencies: ['io.k8s.api.core.v1.Toleration']"""
    nodeSelector: core.optional[dict[str, str]]
    tolerations: core.optional[list[io_k8s_api_core_v1_Toleration]]


@core.schema
class io_k8s_api_rbac_v1_PolicyRule:
    """PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to."""

    """Dependencies: []"""
    apiGroups: core.optional[list[str]]
    nonResourceURLs: core.optional[list[str]]
    resourceNames: core.optional[list[str]]
    resources: core.optional[list[str]]
    verbs: list[str]


@core.schema
class io_k8s_api_rbac_v1_RoleRef:
    """RoleRef contains information that points to the role being used"""

    """Dependencies: []"""
    apiGroup: str
    kind: str
    name: str


@core.schema
class io_k8s_api_rbac_v1_Subject:
    """Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names."""

    """Dependencies: []"""
    apiGroup: core.optional[str]
    kind: str
    name: str
    namespace: core.optional[str]


@core.schema
class io_k8s_api_resource_v1alpha2_NamedResourcesAllocationResult:
    """NamedResourcesAllocationResult is used in AllocationResultModel."""

    """Dependencies: []"""
    name: str


@core.schema
class io_k8s_api_resource_v1alpha2_NamedResourcesFilter:
    """NamedResourcesFilter is used in ResourceFilterModel."""

    """Dependencies: []"""
    selector: str


@core.schema
class io_k8s_api_resource_v1alpha2_NamedResourcesIntSlice:
    """NamedResourcesIntSlice contains a slice of 64-bit integers."""

    """Dependencies: []"""
    ints: list[int]


@core.schema
class io_k8s_api_resource_v1alpha2_NamedResourcesRequest:
    """NamedResourcesRequest is used in ResourceRequestModel."""

    """Dependencies: []"""
    selector: str


@core.schema
class io_k8s_api_resource_v1alpha2_NamedResourcesStringSlice:
    """NamedResourcesStringSlice contains a slice of strings."""

    """Dependencies: []"""
    strings: list[str]


@core.schema
class io_k8s_api_resource_v1alpha2_PodSchedulingContextSpec:
    """PodSchedulingContextSpec describes where resources for the Pod are needed."""

    """Dependencies: []"""
    potentialNodes: core.optional[list[str]]
    selectedNode: core.optional[str]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimConsumerReference:
    """ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim."""

    """Dependencies: []"""
    apiGroup: core.optional[str]
    name: str
    resource: str
    uid: str


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimParametersReference:
    """ResourceClaimParametersReference contains enough information to let you locate the parameters for a ResourceClaim. The object must be in the same namespace as the ResourceClaim."""

    """Dependencies: []"""
    apiGroup: core.optional[str]
    kind: str
    name: str


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimSchedulingStatus:
    """ResourceClaimSchedulingStatus contains information about one particular ResourceClaim with "WaitForFirstConsumer" allocation mode."""

    """Dependencies: []"""
    name: core.optional[str]
    unsuitableNodes: core.optional[list[str]]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimSpec:
    """ResourceClaimSpec defines how a resource is to be allocated."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceClaimParametersReference']"""
    allocationMode: core.optional[str]
    parametersRef: core.optional[
        io_k8s_api_resource_v1alpha2_ResourceClaimParametersReference
    ]
    resourceClassName: str


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClassParametersReference:
    """ResourceClassParametersReference contains enough information to let you locate the parameters for a ResourceClass."""

    """Dependencies: []"""
    apiGroup: core.optional[str]
    kind: str
    name: str
    namespace: core.optional[str]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceFilter:
    """ResourceFilter is a filter for resources from one particular driver."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.NamedResourcesFilter']"""
    driverName: core.optional[str]
    namedResources: core.optional[io_k8s_api_resource_v1alpha2_NamedResourcesFilter]


@core.schema
class io_k8s_api_storage_v1_TokenRequest:
    """TokenRequest contains parameters of a service account token."""

    """Dependencies: []"""
    audience: str
    expirationSeconds: core.optional[int]


@core.schema
class io_k8s_api_storage_v1_VolumeNodeResources:
    """VolumeNodeResources is a set of resource limits for scheduling of volumes."""

    """Dependencies: []"""
    count: core.optional[int]


@core.schema
class io_k8s_api_storagemigration_v1alpha1_GroupVersionResource:
    """The names of the group, the version, and the resource."""

    """Dependencies: []"""
    group: core.optional[str]
    resource: core.optional[str]
    version: core.optional[str]


@core.schema
class io_k8s_api_storagemigration_v1alpha1_StorageVersionMigrationSpec:
    """Spec of the storage version migration."""

    """Dependencies: ['io.k8s.api.storagemigration.v1alpha1.GroupVersionResource']"""
    continueToken: core.optional[str]
    resource: io_k8s_api_storagemigration_v1alpha1_GroupVersionResource


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceColumnDefinition:
    """CustomResourceColumnDefinition specifies a column for server side printing."""

    """Dependencies: []"""
    description: core.optional[str]
    format: core.optional[str]
    jsonPath: str
    name: str
    priority: core.optional[int]
    type: str


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionNames:
    """CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition"""

    """Dependencies: []"""
    categories: core.optional[list[str]]
    kind: str
    listKind: core.optional[str]
    plural: str
    shortNames: core.optional[list[str]]
    singular: core.optional[str]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceSubresourceScale:
    """CustomResourceSubresourceScale defines how to serve the scale subresource for CustomResources."""

    """Dependencies: []"""
    labelSelectorPath: core.optional[str]
    specReplicasPath: str
    statusReplicasPath: str


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceSubresourceStatus:
    """CustomResourceSubresourceStatus defines how to serve the status subresource for CustomResources. Status is represented by the `.status` JSON path inside of a CustomResource. When set, * exposes a /status subresource for the custom resource * PUT requests to the /status subresource take a custom resource object, and ignore changes to anything except the status stanza * PUT/POST/PATCH requests to the custom resource ignore changes to the status stanza"""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceSubresources:
    """CustomResourceSubresources defines the status and scale subresources for CustomResources."""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceSubresourceScale', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceSubresourceStatus']"""
    scale: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceSubresourceScale
    ]
    status: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceSubresourceStatus
    ]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceValidation:
    """CustomResourceValidation is a list of validation methods for CustomResources."""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps']"""
    openAPIV3Schema: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_JSONSchemaProps
    ]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_ExternalDocumentation:
    """ExternalDocumentation allows referencing an external resource for extended documentation."""

    """Dependencies: []"""
    description: core.optional[str]
    url: core.optional[str]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_JSON:
    """JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_JSONSchemaPropsOrArray:
    """JSONSchemaPropsOrArray represents a value that can either be a JSONSchemaProps or an array of JSONSchemaProps. Mainly here for serialization purposes."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_JSONSchemaPropsOrBool:
    """JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_JSONSchemaPropsOrStringArray:
    """JSONSchemaPropsOrStringArray represents a JSONSchemaProps or a string array."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_SelectableField:
    """SelectableField specifies the JSON path of a field that may be used with field selectors."""

    """Dependencies: []"""
    jsonPath: str


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_ServiceReference:
    """ServiceReference holds a reference to Service.legacy.k8s.io"""

    """Dependencies: []"""
    name: str
    namespace: str
    path: core.optional[str]
    port: core.optional[int]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_ValidationRule:
    """ValidationRule describes a validation rule written in the CEL expression language."""

    """Dependencies: []"""
    fieldPath: core.optional[str]
    message: core.optional[str]
    messageExpression: core.optional[str]
    optionalOldSelf: core.optional[bool]
    reason: core.optional[str]
    rule: str


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_WebhookClientConfig:
    """WebhookClientConfig contains the information to make a TLS connection with the webhook."""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.ServiceReference']"""
    caBundle: core.optional[str]
    service: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_ServiceReference
    ]
    url: core.optional[str]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_WebhookConversion:
    """WebhookConversion describes how to call a conversion webhook"""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.WebhookClientConfig']"""
    clientConfig: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_WebhookClientConfig
    ]
    conversionReviewVersions: list[str]


@core.schema
class io_k8s_apimachinery_pkg_api_resource_Quantity:
    """Quantity is a fixed-point representation of a number. It provides convenient marshaling/unmarshaling in JSON and YAML, in addition to String() and AsInt64() accessors.

    The serialization format is:

    ``` <quantity>        ::= <signedNumber><suffix>

            (Note that <suffix> may be empty, from the "" case in <decimalSI>.)

    <digit>           ::= 0 | 1 | ... | 9 <digits>          ::= <digit> | <digit><digits> <number>          ::= <digits> | <digits>.<digits> | <digits>. | .<digits> <sign>            ::= "+" | "-" <signedNumber>    ::= <number> | <sign><number> <suffix>          ::= <binarySI> | <decimalExponent> | <decimalSI> <binarySI>        ::= Ki | Mi | Gi | Ti | Pi | Ei

            (International System of units; See: http://physics.nist.gov/cuu/Units/binary.html)

    <decimalSI>       ::= m | "" | k | M | G | T | P | E

            (Note that 1024 = 1Ki but 1000 = 1k; I didn't choose the capitalization.)

    <decimalExponent> ::= "e" <signedNumber> | "E" <signedNumber> ```

    No matter which of the three exponent forms is used, no quantity may represent a number greater than 2^63-1 in magnitude, nor may it have more than 3 decimal places. Numbers larger or more precise will be capped or rounded up. (E.g.: 0.1m will rounded up to 1m.) This may be extended in the future if we require larger or smaller quantities.

    When a Quantity is parsed from a string, it will remember the type of suffix it had, and will use the same type again when it is serialized.

    Before serializing, Quantity will be put in "canonical form". This means that Exponent/suffix will be adjusted up or down (with a corresponding increase or decrease in Mantissa) such that:

    - No precision is lost - No fractional digits will be emitted - The exponent (or suffix) is as large as possible.

    The sign will be omitted unless the number is negative.

    Examples:

    - 1.5 will be serialized as "1500m" - 1.5Gi will be serialized as "1536Mi"

    Note that the quantity will NEVER be internally represented by a floating point number. That is the whole point of this exercise.

    Non-canonical values will still parse as long as they are well formed, but will be re-emitted in their canonical form. (So always use canonical form, or don't diff.)

    This format is intended to make it difficult to use these numbers without writing some sort of special handling code in the hopes that that will cause implementors to also use a fixed point implementation.
    """

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_APIResource:
    """APIResource specifies the name of a resource and whether it is namespaced."""

    """Dependencies: []"""
    categories: core.optional[list[str]]
    group: core.optional[str]
    kind: str
    name: str
    namespaced: bool
    shortNames: core.optional[list[str]]
    singularName: str
    storageVersionHash: core.optional[str]
    verbs: list[str]
    version: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_APIResourceList:
    """APIResourceList is a list of APIResource, it is used to expose the name of the resources supported in a specific group and version, and if the resource is namespaced."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.APIResource']"""
    apiVersion: core.optional[str]
    groupVersion: str
    kind: core.optional[str]
    resources: list[io_k8s_apimachinery_pkg_apis_meta_v1_APIResource]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_FieldsV1:
    """FieldsV1 stores a set of fields in a data structure like a Trie, in JSON format.

    Each key is either a '.' representing the field itself, and will always map to an empty set, or a string representing a sub-field or item. The string will follow one of these four formats: 'f:<name>', where <name> is the name of a field in a struct, or key in a map 'v:<value>', where <value> is the exact json formatted value of a list item 'i:<index>', where <index> is position of a item in a list 'k:<keys>', where <keys> is a map of  a list item's key fields to their unique values If a key maps to an empty Fields value, the field that key represents is part of the set.

    The exact format is defined in sigs.k8s.io/structured-merge-diff"""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_GroupVersionForDiscovery:
    """GroupVersion contains the "group/version" and "version" string of a version. It is made a struct to keep extensibility."""

    """Dependencies: []"""
    groupVersion: str
    version: str


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelectorRequirement:
    """A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values."""

    """Dependencies: []"""
    key: str
    operator: str
    values: core.optional[list[str]]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta:
    """ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}."""

    """Dependencies: []"""
    continue_: core.optional[str]
    remainingItemCount: core.optional[int]
    resourceVersion: core.optional[str]
    selfLink: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_MicroTime:
    """MicroTime is version of Time with microsecond level precision."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_OwnerReference:
    """OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field."""

    """Dependencies: []"""
    apiVersion: str
    blockOwnerDeletion: core.optional[bool]
    controller: core.optional[bool]
    kind: str
    name: str
    uid: str


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_Patch:
    """Patch is provided to give a concrete name and type to the Kubernetes PATCH request body."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_Preconditions:
    """Preconditions must be fulfilled before an operation (update, delete, etc.) is carried out."""

    """Dependencies: []"""
    resourceVersion: core.optional[str]
    uid: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_ServerAddressByClientCIDR:
    """ServerAddressByClientCIDR helps the client to determine the server address that they should use, depending on the clientCIDR that they match."""

    """Dependencies: []"""
    clientCIDR: str
    serverAddress: str


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_StatusCause:
    """StatusCause provides more information about an api.Status failure, including cases when multiple errors are encountered."""

    """Dependencies: []"""
    field: core.optional[str]
    message: core.optional[str]
    reason: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_StatusDetails:
    """StatusDetails is a set of additional properties that MAY be set by the server to provide additional information about a response. The Reason field of a Status object defines what attributes will be set. Clients must ignore fields that do not match the defined type of each attribute, and should assume that any attribute may be empty, invalid, or under defined."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.StatusCause']"""
    causes: core.optional[list[io_k8s_apimachinery_pkg_apis_meta_v1_StatusCause]]
    group: core.optional[str]
    kind: core.optional[str]
    name: core.optional[str]
    retryAfterSeconds: core.optional[int]
    uid: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_Time:
    """Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apimachinery_pkg_runtime_RawExtension:
    """RawExtension is used to hold extensions in external versions.

    To use this, make a field which has RawExtension as its type in your external, versioned struct, and Object in your internal struct. You also need to register your various plugin types.

    // Internal package:

            type MyAPIObject struct {
                    runtime.TypeMeta `json:",inline"`
                    MyPlugin runtime.Object `json:"myPlugin"`
            }

            type PluginA struct {
                    AOption string `json:"aOption"`
            }

    // External package:

            type MyAPIObject struct {
                    runtime.TypeMeta `json:",inline"`
                    MyPlugin runtime.RawExtension `json:"myPlugin"`
            }

            type PluginA struct {
                    AOption string `json:"aOption"`
            }

    // On the wire, the JSON will look something like this:

            {
                    "kind":"MyAPIObject",
                    "apiVersion":"v1",
                    "myPlugin": {
                            "kind":"PluginA",
                            "aOption":"foo",
                    },
            }

    So what happens? Decode first uses json or yaml to unmarshal the serialized data into your external MyAPIObject. That causes the raw JSON to be stored, but not unpacked. The next step is to copy (using pkg/conversion) into the internal struct. The runtime package's DefaultScheme has conversion functions installed which will unpack the JSON stored in RawExtension, turning it into the correct object type, and storing it in the Object. (TODO: In the case where the object is of an unknown type, a runtime.Unknown object will be created and stored.)
    """

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apimachinery_pkg_util_intstr_IntOrString:
    """IntOrString is a type that can hold an int32 or a string.  When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a name or number."""

    """Dependencies: []"""
    pass


@core.schema
class io_k8s_apimachinery_pkg_version_Info:
    """Info contains versioning information. how we'll want to distribute that information."""

    """Dependencies: []"""
    buildDate: str
    compiler: str
    gitCommit: str
    gitTreeState: str
    gitVersion: str
    goVersion: str
    major: str
    minor: str
    platform: str


@core.schema
class io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIServiceCondition:
    """APIServiceCondition describes the state of an APIService at a particular point"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIServiceStatus:
    """APIServiceStatus contains derived information about an API server"""

    """Dependencies: ['io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.APIServiceCondition']"""
    conditions: core.optional[
        list[io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIServiceCondition]
    ]


@core.schema
class io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_ServiceReference:
    """ServiceReference holds a reference to Service.legacy.k8s.io"""

    """Dependencies: []"""
    name: core.optional[str]
    namespace: core.optional[str]
    port: core.optional[int]


@core.schema
class io_k8s_api_apiserverinternal_v1alpha1_StorageVersionCondition:
    """Describes the state of the storageVersion at a certain point."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: str
    observedGeneration: core.optional[int]
    reason: str
    status: str
    type: str


@core.schema
class io_k8s_api_apiserverinternal_v1alpha1_StorageVersionStatus:
    """API server instances report the versions they can decode and the version they encode objects to when persisting objects in the backend."""

    """Dependencies: ['io.k8s.api.apiserverinternal.v1alpha1.StorageVersionCondition', 'io.k8s.api.apiserverinternal.v1alpha1.ServerStorageVersion']"""
    commonEncodingVersion: core.optional[str]
    conditions: core.optional[
        list[io_k8s_api_apiserverinternal_v1alpha1_StorageVersionCondition]
    ]
    storageVersions: core.optional[
        list[io_k8s_api_apiserverinternal_v1alpha1_ServerStorageVersion]
    ]


@core.schema
class io_k8s_api_apps_v1_DaemonSetCondition:
    """DaemonSetCondition describes the state of a DaemonSet at a certain point."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_apps_v1_DaemonSetStatus:
    """DaemonSetStatus represents the current status of a daemon set."""

    """Dependencies: ['io.k8s.api.apps.v1.DaemonSetCondition']"""
    collisionCount: core.optional[int]
    conditions: core.optional[list[io_k8s_api_apps_v1_DaemonSetCondition]]
    currentNumberScheduled: int
    desiredNumberScheduled: int
    numberAvailable: core.optional[int]
    numberMisscheduled: int
    numberReady: int
    numberUnavailable: core.optional[int]
    observedGeneration: core.optional[int]
    updatedNumberScheduled: core.optional[int]


@core.schema
class io_k8s_api_apps_v1_DeploymentCondition:
    """DeploymentCondition describes the state of a deployment at a certain point."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    lastUpdateTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_apps_v1_DeploymentStatus:
    """DeploymentStatus is the most recently observed status of the Deployment."""

    """Dependencies: ['io.k8s.api.apps.v1.DeploymentCondition']"""
    availableReplicas: core.optional[int]
    collisionCount: core.optional[int]
    conditions: core.optional[list[io_k8s_api_apps_v1_DeploymentCondition]]
    observedGeneration: core.optional[int]
    readyReplicas: core.optional[int]
    replicas: core.optional[int]
    unavailableReplicas: core.optional[int]
    updatedReplicas: core.optional[int]


@core.schema
class io_k8s_api_apps_v1_ReplicaSetCondition:
    """ReplicaSetCondition describes the state of a replica set at a certain point."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_apps_v1_ReplicaSetStatus:
    """ReplicaSetStatus represents the current status of a ReplicaSet."""

    """Dependencies: ['io.k8s.api.apps.v1.ReplicaSetCondition']"""
    availableReplicas: core.optional[int]
    conditions: core.optional[list[io_k8s_api_apps_v1_ReplicaSetCondition]]
    fullyLabeledReplicas: core.optional[int]
    observedGeneration: core.optional[int]
    readyReplicas: core.optional[int]
    replicas: int


@core.schema
class io_k8s_api_apps_v1_RollingUpdateDaemonSet:
    """Spec to control the desired behavior of daemon set rolling update."""

    """Dependencies: ['io.k8s.apimachinery.pkg.util.intstr.IntOrString', 'io.k8s.apimachinery.pkg.util.intstr.IntOrString']"""
    maxSurge: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]
    maxUnavailable: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]


@core.schema
class io_k8s_api_apps_v1_RollingUpdateDeployment:
    """Spec to control the desired behavior of rolling update."""

    """Dependencies: ['io.k8s.apimachinery.pkg.util.intstr.IntOrString', 'io.k8s.apimachinery.pkg.util.intstr.IntOrString']"""
    maxSurge: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]
    maxUnavailable: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]


@core.schema
class io_k8s_api_apps_v1_RollingUpdateStatefulSetStrategy:
    """RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType."""

    """Dependencies: ['io.k8s.apimachinery.pkg.util.intstr.IntOrString']"""
    maxUnavailable: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]
    partition: core.optional[int]


@core.schema
class io_k8s_api_apps_v1_StatefulSetCondition:
    """StatefulSetCondition describes the state of a statefulset at a certain point."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_apps_v1_StatefulSetStatus:
    """StatefulSetStatus represents the current state of a StatefulSet."""

    """Dependencies: ['io.k8s.api.apps.v1.StatefulSetCondition']"""
    availableReplicas: core.optional[int]
    collisionCount: core.optional[int]
    conditions: core.optional[list[io_k8s_api_apps_v1_StatefulSetCondition]]
    currentReplicas: core.optional[int]
    currentRevision: core.optional[str]
    observedGeneration: core.optional[int]
    readyReplicas: core.optional[int]
    replicas: int
    updateRevision: core.optional[str]
    updatedReplicas: core.optional[int]


@core.schema
class io_k8s_api_apps_v1_StatefulSetUpdateStrategy:
    """StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy."""

    """Dependencies: ['io.k8s.api.apps.v1.RollingUpdateStatefulSetStrategy']"""
    rollingUpdate: core.optional[io_k8s_api_apps_v1_RollingUpdateStatefulSetStrategy]
    type: core.optional[str]


@core.schema
class io_k8s_api_authentication_v1_SelfSubjectReviewStatus:
    """SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user."""

    """Dependencies: ['io.k8s.api.authentication.v1.UserInfo']"""
    userInfo: core.optional[io_k8s_api_authentication_v1_UserInfo]


@core.schema
class io_k8s_api_authentication_v1_TokenRequestStatus:
    """TokenRequestStatus is the result of a token request."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    expirationTimestamp: io_k8s_apimachinery_pkg_apis_meta_v1_Time
    token: str


@core.schema
class io_k8s_api_authentication_v1_TokenReviewStatus:
    """TokenReviewStatus is the result of the token authentication request."""

    """Dependencies: ['io.k8s.api.authentication.v1.UserInfo']"""
    audiences: core.optional[list[str]]
    authenticated: core.optional[bool]
    error: core.optional[str]
    user: core.optional[io_k8s_api_authentication_v1_UserInfo]


@core.schema
class io_k8s_api_autoscaling_v1_HorizontalPodAutoscalerStatus:
    """current status of a horizontal pod autoscaler"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    currentCPUUtilizationPercentage: core.optional[int]
    currentReplicas: int
    desiredReplicas: int
    lastScaleTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    observedGeneration: core.optional[int]


@core.schema
class io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerCondition:
    """HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_autoscaling_v2_MetricTarget:
    """MetricTarget defines the target value, average value, or average utilization of a specific metric"""

    """Dependencies: ['io.k8s.apimachinery.pkg.api.resource.Quantity', 'io.k8s.apimachinery.pkg.api.resource.Quantity']"""
    averageUtilization: core.optional[int]
    averageValue: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]
    type: str
    value: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]


@core.schema
class io_k8s_api_autoscaling_v2_MetricValueStatus:
    """MetricValueStatus holds the current value for a metric"""

    """Dependencies: ['io.k8s.apimachinery.pkg.api.resource.Quantity', 'io.k8s.apimachinery.pkg.api.resource.Quantity']"""
    averageUtilization: core.optional[int]
    averageValue: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]
    value: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]


@core.schema
class io_k8s_api_autoscaling_v2_ResourceMetricSource:
    """ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values will be averaged together before being compared to the target.  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.  Only one "target" type should be set."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricTarget']"""
    name: str
    target: io_k8s_api_autoscaling_v2_MetricTarget


@core.schema
class io_k8s_api_autoscaling_v2_ResourceMetricStatus:
    """ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricValueStatus']"""
    current: io_k8s_api_autoscaling_v2_MetricValueStatus
    name: str


@core.schema
class io_k8s_api_batch_v1_CronJobStatus:
    """CronJobStatus represents the current state of a cron job."""

    """Dependencies: ['io.k8s.api.core.v1.ObjectReference', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    active: core.optional[list[io_k8s_api_core_v1_ObjectReference]]
    lastScheduleTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    lastSuccessfulTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]


@core.schema
class io_k8s_api_batch_v1_JobCondition:
    """JobCondition describes current state of a job."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastProbeTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_batch_v1_JobStatus:
    """JobStatus represents the current state of a Job."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.api.batch.v1.JobCondition', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.api.batch.v1.UncountedTerminatedPods']"""
    active: core.optional[int]
    completedIndexes: core.optional[str]
    completionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    conditions: core.optional[list[io_k8s_api_batch_v1_JobCondition]]
    failed: core.optional[int]
    failedIndexes: core.optional[str]
    ready: core.optional[int]
    startTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    succeeded: core.optional[int]
    terminating: core.optional[int]
    uncountedTerminatedPods: core.optional[io_k8s_api_batch_v1_UncountedTerminatedPods]


@core.schema
class io_k8s_api_batch_v1_PodFailurePolicy:
    """PodFailurePolicy describes how failed pods influence the backoffLimit."""

    """Dependencies: ['io.k8s.api.batch.v1.PodFailurePolicyRule']"""
    rules: list[io_k8s_api_batch_v1_PodFailurePolicyRule]


@core.schema
class io_k8s_api_batch_v1_SuccessPolicy:
    """SuccessPolicy describes when a Job can be declared as succeeded based on the success of some indexes."""

    """Dependencies: ['io.k8s.api.batch.v1.SuccessPolicyRule']"""
    rules: list[io_k8s_api_batch_v1_SuccessPolicyRule]


@core.schema
class io_k8s_api_certificates_v1_CertificateSigningRequestCondition:
    """CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    lastUpdateTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_certificates_v1_CertificateSigningRequestStatus:
    """CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate."""

    """Dependencies: ['io.k8s.api.certificates.v1.CertificateSigningRequestCondition']"""
    certificate: core.optional[str]
    conditions: core.optional[
        list[io_k8s_api_certificates_v1_CertificateSigningRequestCondition]
    ]


@core.schema
class io_k8s_api_coordination_v1_LeaseSpec:
    """LeaseSpec is a specification of a Lease."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime', 'io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime']"""
    acquireTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_MicroTime]
    holderIdentity: core.optional[str]
    leaseDurationSeconds: core.optional[int]
    leaseTransitions: core.optional[int]
    renewTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_MicroTime]


@core.schema
class io_k8s_api_core_v1_CSIPersistentVolumeSource:
    """Represents storage that is managed by an external CSI volume driver (Beta feature)"""

    """Dependencies: ['io.k8s.api.core.v1.SecretReference', 'io.k8s.api.core.v1.SecretReference', 'io.k8s.api.core.v1.SecretReference', 'io.k8s.api.core.v1.SecretReference', 'io.k8s.api.core.v1.SecretReference']"""
    controllerExpandSecretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    controllerPublishSecretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    driver: str
    fsType: core.optional[str]
    nodeExpandSecretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    nodePublishSecretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    nodeStageSecretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    readOnly: core.optional[bool]
    volumeAttributes: core.optional[dict[str, str]]
    volumeHandle: str


@core.schema
class io_k8s_api_core_v1_CSIVolumeSource:
    """Represents a source location of a volume to mount, managed by an external CSI driver"""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference']"""
    driver: str
    fsType: core.optional[str]
    nodePublishSecretRef: core.optional[io_k8s_api_core_v1_LocalObjectReference]
    readOnly: core.optional[bool]
    volumeAttributes: core.optional[dict[str, str]]


@core.schema
class io_k8s_api_core_v1_CephFSPersistentVolumeSource:
    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.SecretReference']"""
    monitors: list[str]
    path: core.optional[str]
    readOnly: core.optional[bool]
    secretFile: core.optional[str]
    secretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    user: core.optional[str]


@core.schema
class io_k8s_api_core_v1_CephFSVolumeSource:
    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference']"""
    monitors: list[str]
    path: core.optional[str]
    readOnly: core.optional[bool]
    secretFile: core.optional[str]
    secretRef: core.optional[io_k8s_api_core_v1_LocalObjectReference]
    user: core.optional[str]


@core.schema
class io_k8s_api_core_v1_CinderPersistentVolumeSource:
    """Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.SecretReference']"""
    fsType: core.optional[str]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    volumeID: str


@core.schema
class io_k8s_api_core_v1_CinderVolumeSource:
    """Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference']"""
    fsType: core.optional[str]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_LocalObjectReference]
    volumeID: str


@core.schema
class io_k8s_api_core_v1_ConfigMapProjection:
    """Adapts a ConfigMap into a projected volume.

    The contents of the target ConfigMap's Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode.
    """

    """Dependencies: ['io.k8s.api.core.v1.KeyToPath']"""
    items: core.optional[list[io_k8s_api_core_v1_KeyToPath]]
    name: core.optional[str]
    optional: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_ConfigMapVolumeSource:
    """Adapts a ConfigMap into a volume.

    The contents of the target ConfigMap's Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.
    """

    """Dependencies: ['io.k8s.api.core.v1.KeyToPath']"""
    defaultMode: core.optional[int]
    items: core.optional[list[io_k8s_api_core_v1_KeyToPath]]
    name: core.optional[str]
    optional: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_ContainerStateRunning:
    """ContainerStateRunning is a running state of a container."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    startedAt: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]


@core.schema
class io_k8s_api_core_v1_ContainerStateTerminated:
    """ContainerStateTerminated is a terminated state of a container."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    containerID: core.optional[str]
    exitCode: int
    finishedAt: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    signal: core.optional[int]
    startedAt: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]


@core.schema
class io_k8s_api_core_v1_ContainerUser:
    """ContainerUser represents user identity information"""

    """Dependencies: ['io.k8s.api.core.v1.LinuxContainerUser']"""
    linux: core.optional[io_k8s_api_core_v1_LinuxContainerUser]


@core.schema
class io_k8s_api_core_v1_EmptyDirVolumeSource:
    """Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling."""

    """Dependencies: ['io.k8s.apimachinery.pkg.api.resource.Quantity']"""
    medium: core.optional[str]
    sizeLimit: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]


@core.schema
class io_k8s_api_core_v1_EndpointAddress:
    """EndpointAddress is a tuple that describes single IP address."""

    """Dependencies: ['io.k8s.api.core.v1.ObjectReference']"""
    hostname: core.optional[str]
    ip: str
    nodeName: core.optional[str]
    targetRef: core.optional[io_k8s_api_core_v1_ObjectReference]


@core.schema
class io_k8s_api_core_v1_EndpointSubset:
    """EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:

            {
              Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
              Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
            }

    The resulting set of endpoints can be viewed as:

            a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
            b: [ 10.10.1.1:309, 10.10.2.2:309 ]"""

    """Dependencies: ['io.k8s.api.core.v1.EndpointAddress', 'io.k8s.api.core.v1.EndpointAddress', 'io.k8s.api.core.v1.EndpointPort']"""
    addresses: core.optional[list[io_k8s_api_core_v1_EndpointAddress]]
    notReadyAddresses: core.optional[list[io_k8s_api_core_v1_EndpointAddress]]
    ports: core.optional[list[io_k8s_api_core_v1_EndpointPort]]


@core.schema
class io_k8s_api_core_v1_EnvFromSource:
    """EnvFromSource represents the source of a set of ConfigMaps"""

    """Dependencies: ['io.k8s.api.core.v1.ConfigMapEnvSource', 'io.k8s.api.core.v1.SecretEnvSource']"""
    configMapRef: core.optional[io_k8s_api_core_v1_ConfigMapEnvSource]
    prefix: core.optional[str]
    secretRef: core.optional[io_k8s_api_core_v1_SecretEnvSource]


@core.schema
class io_k8s_api_core_v1_EventSeries:
    """EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime']"""
    count: core.optional[int]
    lastObservedTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_MicroTime]


@core.schema
class io_k8s_api_core_v1_FlexPersistentVolumeSource:
    """FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin."""

    """Dependencies: ['io.k8s.api.core.v1.SecretReference']"""
    driver: str
    fsType: core.optional[str]
    options: core.optional[dict[str, str]]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_SecretReference]


@core.schema
class io_k8s_api_core_v1_FlexVolumeSource:
    """FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin."""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference']"""
    driver: str
    fsType: core.optional[str]
    options: core.optional[dict[str, str]]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_LocalObjectReference]


@core.schema
class io_k8s_api_core_v1_HTTPGetAction:
    """HTTPGetAction describes an action based on HTTP Get requests."""

    """Dependencies: ['io.k8s.api.core.v1.HTTPHeader', 'io.k8s.apimachinery.pkg.util.intstr.IntOrString']"""
    host: core.optional[str]
    httpHeaders: core.optional[list[io_k8s_api_core_v1_HTTPHeader]]
    path: core.optional[str]
    port: io_k8s_apimachinery_pkg_util_intstr_IntOrString
    scheme: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ISCSIPersistentVolumeSource:
    """ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.SecretReference']"""
    chapAuthDiscovery: core.optional[bool]
    chapAuthSession: core.optional[bool]
    fsType: core.optional[str]
    initiatorName: core.optional[str]
    iqn: str
    iscsiInterface: core.optional[str]
    lun: int
    portals: core.optional[list[str]]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    targetPortal: str


@core.schema
class io_k8s_api_core_v1_ISCSIVolumeSource:
    """Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference']"""
    chapAuthDiscovery: core.optional[bool]
    chapAuthSession: core.optional[bool]
    fsType: core.optional[str]
    initiatorName: core.optional[str]
    iqn: str
    iscsiInterface: core.optional[str]
    lun: int
    portals: core.optional[list[str]]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_LocalObjectReference]
    targetPortal: str


@core.schema
class io_k8s_api_core_v1_LoadBalancerIngress:
    """LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended for the service should be sent to an ingress point."""

    """Dependencies: ['io.k8s.api.core.v1.PortStatus']"""
    hostname: core.optional[str]
    ip: core.optional[str]
    ipMode: core.optional[str]
    ports: core.optional[list[io_k8s_api_core_v1_PortStatus]]


@core.schema
class io_k8s_api_core_v1_LoadBalancerStatus:
    """LoadBalancerStatus represents the status of a load-balancer."""

    """Dependencies: ['io.k8s.api.core.v1.LoadBalancerIngress']"""
    ingress: core.optional[list[io_k8s_api_core_v1_LoadBalancerIngress]]


@core.schema
class io_k8s_api_core_v1_NamespaceCondition:
    """NamespaceCondition contains details about state of namespace."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_core_v1_NamespaceStatus:
    """NamespaceStatus is information about the current status of a Namespace."""

    """Dependencies: ['io.k8s.api.core.v1.NamespaceCondition']"""
    conditions: core.optional[list[io_k8s_api_core_v1_NamespaceCondition]]
    phase: core.optional[str]


@core.schema
class io_k8s_api_core_v1_NodeCondition:
    """NodeCondition contains condition information for a node."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastHeartbeatTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_core_v1_NodeRuntimeHandler:
    """NodeRuntimeHandler is a set of runtime handler information."""

    """Dependencies: ['io.k8s.api.core.v1.NodeRuntimeHandlerFeatures']"""
    features: core.optional[io_k8s_api_core_v1_NodeRuntimeHandlerFeatures]
    name: core.optional[str]


@core.schema
class io_k8s_api_core_v1_NodeSelector:
    """A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms."""

    """Dependencies: ['io.k8s.api.core.v1.NodeSelectorTerm']"""
    nodeSelectorTerms: list[io_k8s_api_core_v1_NodeSelectorTerm]


@core.schema
class io_k8s_api_core_v1_NodeStatus:
    """NodeStatus is information about the current status of a node."""

    """Dependencies: ['io.k8s.api.core.v1.NodeAddress', 'io.k8s.api.core.v1.NodeCondition', 'io.k8s.api.core.v1.NodeConfigStatus', 'io.k8s.api.core.v1.NodeDaemonEndpoints', 'io.k8s.api.core.v1.ContainerImage', 'io.k8s.api.core.v1.NodeSystemInfo', 'io.k8s.api.core.v1.NodeRuntimeHandler', 'io.k8s.api.core.v1.AttachedVolume']"""
    addresses: core.optional[list[io_k8s_api_core_v1_NodeAddress]]
    allocatable: core.optional[dict[str, str]]
    capacity: core.optional[dict[str, str]]
    conditions: core.optional[list[io_k8s_api_core_v1_NodeCondition]]
    config: core.optional[io_k8s_api_core_v1_NodeConfigStatus]
    daemonEndpoints: core.optional[io_k8s_api_core_v1_NodeDaemonEndpoints]
    images: core.optional[list[io_k8s_api_core_v1_ContainerImage]]
    nodeInfo: core.optional[io_k8s_api_core_v1_NodeSystemInfo]
    phase: core.optional[str]
    runtimeHandlers: core.optional[list[io_k8s_api_core_v1_NodeRuntimeHandler]]
    volumesAttached: core.optional[list[io_k8s_api_core_v1_AttachedVolume]]
    volumesInUse: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_PersistentVolumeClaimCondition:
    """PersistentVolumeClaimCondition contains details about state of pvc"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastProbeTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_core_v1_PersistentVolumeClaimStatus:
    """PersistentVolumeClaimStatus is the current status of a persistent volume claim."""

    """Dependencies: ['io.k8s.api.core.v1.PersistentVolumeClaimCondition', 'io.k8s.api.core.v1.ModifyVolumeStatus']"""
    accessModes: core.optional[list[str]]
    allocatedResourceStatuses: core.optional[dict[str, str]]
    allocatedResources: core.optional[dict[str, str]]
    capacity: core.optional[dict[str, str]]
    conditions: core.optional[list[io_k8s_api_core_v1_PersistentVolumeClaimCondition]]
    currentVolumeAttributesClassName: core.optional[str]
    modifyVolumeStatus: core.optional[io_k8s_api_core_v1_ModifyVolumeStatus]
    phase: core.optional[str]


@core.schema
class io_k8s_api_core_v1_PersistentVolumeStatus:
    """PersistentVolumeStatus is the current status of a persistent volume."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastPhaseTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    phase: core.optional[str]
    reason: core.optional[str]


@core.schema
class io_k8s_api_core_v1_PodCondition:
    """PodCondition contains details for the current condition of this pod."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastProbeTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_core_v1_PodDNSConfig:
    """PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy."""

    """Dependencies: ['io.k8s.api.core.v1.PodDNSConfigOption']"""
    nameservers: core.optional[list[str]]
    options: core.optional[list[io_k8s_api_core_v1_PodDNSConfigOption]]
    searches: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_PodSecurityContext:
    """PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext.  Field values of container.securityContext take precedence over field values of PodSecurityContext."""

    """Dependencies: ['io.k8s.api.core.v1.AppArmorProfile', 'io.k8s.api.core.v1.SELinuxOptions', 'io.k8s.api.core.v1.SeccompProfile', 'io.k8s.api.core.v1.Sysctl', 'io.k8s.api.core.v1.WindowsSecurityContextOptions']"""
    appArmorProfile: core.optional[io_k8s_api_core_v1_AppArmorProfile]
    fsGroup: core.optional[int]
    fsGroupChangePolicy: core.optional[str]
    runAsGroup: core.optional[int]
    runAsNonRoot: core.optional[bool]
    runAsUser: core.optional[int]
    seLinuxOptions: core.optional[io_k8s_api_core_v1_SELinuxOptions]
    seccompProfile: core.optional[io_k8s_api_core_v1_SeccompProfile]
    supplementalGroups: core.optional[list[int]]
    supplementalGroupsPolicy: core.optional[str]
    sysctls: core.optional[list[io_k8s_api_core_v1_Sysctl]]
    windowsOptions: core.optional[io_k8s_api_core_v1_WindowsSecurityContextOptions]


@core.schema
class io_k8s_api_core_v1_RBDPersistentVolumeSource:
    """Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.SecretReference']"""
    fsType: core.optional[str]
    image: str
    keyring: core.optional[str]
    monitors: list[str]
    pool: core.optional[str]
    readOnly: core.optional[bool]
    secretRef: core.optional[io_k8s_api_core_v1_SecretReference]
    user: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ReplicationControllerCondition:
    """ReplicationControllerCondition describes the state of a replication controller at a certain point."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_core_v1_ReplicationControllerStatus:
    """ReplicationControllerStatus represents the current status of a replication controller."""

    """Dependencies: ['io.k8s.api.core.v1.ReplicationControllerCondition']"""
    availableReplicas: core.optional[int]
    conditions: core.optional[list[io_k8s_api_core_v1_ReplicationControllerCondition]]
    fullyLabeledReplicas: core.optional[int]
    observedGeneration: core.optional[int]
    readyReplicas: core.optional[int]
    replicas: int


@core.schema
class io_k8s_api_core_v1_ResourceFieldSelector:
    """ResourceFieldSelector represents container resources (cpu, memory) and their output format"""

    """Dependencies: ['io.k8s.apimachinery.pkg.api.resource.Quantity']"""
    containerName: core.optional[str]
    divisor: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]
    resource: str


@core.schema
class io_k8s_api_core_v1_ScaleIOPersistentVolumeSource:
    """ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume"""

    """Dependencies: ['io.k8s.api.core.v1.SecretReference']"""
    fsType: core.optional[str]
    gateway: str
    protectionDomain: core.optional[str]
    readOnly: core.optional[bool]
    secretRef: io_k8s_api_core_v1_SecretReference
    sslEnabled: core.optional[bool]
    storageMode: core.optional[str]
    storagePool: core.optional[str]
    system: str
    volumeName: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ScopeSelector:
    """A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements."""

    """Dependencies: ['io.k8s.api.core.v1.ScopedResourceSelectorRequirement']"""
    matchExpressions: core.optional[
        list[io_k8s_api_core_v1_ScopedResourceSelectorRequirement]
    ]


@core.schema
class io_k8s_api_core_v1_SecurityContext:
    """SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext.  When both are set, the values in SecurityContext take precedence."""

    """Dependencies: ['io.k8s.api.core.v1.AppArmorProfile', 'io.k8s.api.core.v1.Capabilities', 'io.k8s.api.core.v1.SELinuxOptions', 'io.k8s.api.core.v1.SeccompProfile', 'io.k8s.api.core.v1.WindowsSecurityContextOptions']"""
    allowPrivilegeEscalation: core.optional[bool]
    appArmorProfile: core.optional[io_k8s_api_core_v1_AppArmorProfile]
    capabilities: core.optional[io_k8s_api_core_v1_Capabilities]
    privileged: core.optional[bool]
    procMount: core.optional[str]
    readOnlyRootFilesystem: core.optional[bool]
    runAsGroup: core.optional[int]
    runAsNonRoot: core.optional[bool]
    runAsUser: core.optional[int]
    seLinuxOptions: core.optional[io_k8s_api_core_v1_SELinuxOptions]
    seccompProfile: core.optional[io_k8s_api_core_v1_SeccompProfile]
    windowsOptions: core.optional[io_k8s_api_core_v1_WindowsSecurityContextOptions]


@core.schema
class io_k8s_api_core_v1_ServicePort:
    """ServicePort contains information on service's port."""

    """Dependencies: ['io.k8s.apimachinery.pkg.util.intstr.IntOrString']"""
    appProtocol: core.optional[str]
    name: core.optional[str]
    nodePort: core.optional[int]
    port: int
    protocol: core.optional[str]
    targetPort: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]


@core.schema
class io_k8s_api_core_v1_ServiceSpec:
    """ServiceSpec describes the attributes that a user creates on a service."""

    """Dependencies: ['io.k8s.api.core.v1.ServicePort', 'io.k8s.api.core.v1.SessionAffinityConfig']"""
    allocateLoadBalancerNodePorts: core.optional[bool]
    clusterIP: core.optional[str]
    clusterIPs: core.optional[list[str]]
    externalIPs: core.optional[list[str]]
    externalName: core.optional[str]
    externalTrafficPolicy: core.optional[str]
    healthCheckNodePort: core.optional[int]
    internalTrafficPolicy: core.optional[str]
    ipFamilies: core.optional[list[str]]
    ipFamilyPolicy: core.optional[str]
    loadBalancerClass: core.optional[str]
    loadBalancerIP: core.optional[str]
    loadBalancerSourceRanges: core.optional[list[str]]
    ports: core.optional[list[io_k8s_api_core_v1_ServicePort]]
    publishNotReadyAddresses: core.optional[bool]
    selector: core.optional[dict[str, str]]
    sessionAffinity: core.optional[str]
    sessionAffinityConfig: core.optional[io_k8s_api_core_v1_SessionAffinityConfig]
    trafficDistribution: core.optional[str]
    type: core.optional[str]


@core.schema
class io_k8s_api_core_v1_TCPSocketAction:
    """TCPSocketAction describes an action based on opening a socket"""

    """Dependencies: ['io.k8s.apimachinery.pkg.util.intstr.IntOrString']"""
    host: core.optional[str]
    port: io_k8s_apimachinery_pkg_util_intstr_IntOrString


@core.schema
class io_k8s_api_core_v1_Taint:
    """The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    effect: str
    key: str
    timeAdded: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    value: core.optional[str]


@core.schema
class io_k8s_api_core_v1_VolumeNodeAffinity:
    """VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from."""

    """Dependencies: ['io.k8s.api.core.v1.NodeSelector']"""
    required: core.optional[io_k8s_api_core_v1_NodeSelector]


@core.schema
class io_k8s_api_discovery_v1_EndpointHints:
    """EndpointHints provides hints describing how an endpoint should be consumed."""

    """Dependencies: ['io.k8s.api.discovery.v1.ForZone']"""
    forZones: core.optional[list[io_k8s_api_discovery_v1_ForZone]]


@core.schema
class io_k8s_api_events_v1_EventSeries:
    """EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime']"""
    count: int
    lastObservedTime: io_k8s_apimachinery_pkg_apis_meta_v1_MicroTime


@core.schema
class io_k8s_api_flowcontrol_v1_FlowSchemaCondition:
    """FlowSchemaCondition describes conditions for a FlowSchema."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: core.optional[str]
    type: core.optional[str]


@core.schema
class io_k8s_api_flowcontrol_v1_FlowSchemaStatus:
    """FlowSchemaStatus represents the current state of a FlowSchema."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.FlowSchemaCondition']"""
    conditions: core.optional[list[io_k8s_api_flowcontrol_v1_FlowSchemaCondition]]


@core.schema
class io_k8s_api_flowcontrol_v1_LimitResponse:
    """LimitResponse defines how to handle requests that can not be executed right now."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.QueuingConfiguration']"""
    queuing: core.optional[io_k8s_api_flowcontrol_v1_QueuingConfiguration]
    type: str


@core.schema
class io_k8s_api_flowcontrol_v1_LimitedPriorityLevelConfiguration:
    """LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues:
    - How are requests for this priority level limited?
    - What should be done with requests that exceed the limit?"""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.LimitResponse']"""
    borrowingLimitPercent: core.optional[int]
    lendablePercent: core.optional[int]
    limitResponse: core.optional[io_k8s_api_flowcontrol_v1_LimitResponse]
    nominalConcurrencyShares: core.optional[int]


@core.schema
class io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationCondition:
    """PriorityLevelConfigurationCondition defines the condition of priority level."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: core.optional[str]
    type: core.optional[str]


@core.schema
class io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationSpec:
    """PriorityLevelConfigurationSpec specifies the configuration of a priority level."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.ExemptPriorityLevelConfiguration', 'io.k8s.api.flowcontrol.v1.LimitedPriorityLevelConfiguration']"""
    exempt: core.optional[io_k8s_api_flowcontrol_v1_ExemptPriorityLevelConfiguration]
    limited: core.optional[io_k8s_api_flowcontrol_v1_LimitedPriorityLevelConfiguration]
    type: str


@core.schema
class io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationStatus:
    """PriorityLevelConfigurationStatus represents the current state of a "request-priority"."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationCondition']"""
    conditions: core.optional[
        list[io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationCondition]
    ]


@core.schema
class io_k8s_api_flowcontrol_v1_Subject:
    """Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.GroupSubject', 'io.k8s.api.flowcontrol.v1.ServiceAccountSubject', 'io.k8s.api.flowcontrol.v1.UserSubject']"""
    group: core.optional[io_k8s_api_flowcontrol_v1_GroupSubject]
    kind: str
    serviceAccount: core.optional[io_k8s_api_flowcontrol_v1_ServiceAccountSubject]
    user: core.optional[io_k8s_api_flowcontrol_v1_UserSubject]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_FlowSchemaCondition:
    """FlowSchemaCondition describes conditions for a FlowSchema."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: core.optional[str]
    type: core.optional[str]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_FlowSchemaStatus:
    """FlowSchemaStatus represents the current state of a FlowSchema."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.FlowSchemaCondition']"""
    conditions: core.optional[list[io_k8s_api_flowcontrol_v1beta3_FlowSchemaCondition]]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_LimitResponse:
    """LimitResponse defines how to handle requests that can not be executed right now."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.QueuingConfiguration']"""
    queuing: core.optional[io_k8s_api_flowcontrol_v1beta3_QueuingConfiguration]
    type: str


@core.schema
class io_k8s_api_flowcontrol_v1beta3_LimitedPriorityLevelConfiguration:
    """LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues:
    - How are requests for this priority level limited?
    - What should be done with requests that exceed the limit?"""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.LimitResponse']"""
    borrowingLimitPercent: core.optional[int]
    lendablePercent: core.optional[int]
    limitResponse: core.optional[io_k8s_api_flowcontrol_v1beta3_LimitResponse]
    nominalConcurrencyShares: core.optional[int]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationCondition:
    """PriorityLevelConfigurationCondition defines the condition of priority level."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: core.optional[str]
    type: core.optional[str]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationSpec:
    """PriorityLevelConfigurationSpec specifies the configuration of a priority level."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.ExemptPriorityLevelConfiguration', 'io.k8s.api.flowcontrol.v1beta3.LimitedPriorityLevelConfiguration']"""
    exempt: core.optional[
        io_k8s_api_flowcontrol_v1beta3_ExemptPriorityLevelConfiguration
    ]
    limited: core.optional[
        io_k8s_api_flowcontrol_v1beta3_LimitedPriorityLevelConfiguration
    ]
    type: str


@core.schema
class io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationStatus:
    """PriorityLevelConfigurationStatus represents the current state of a "request-priority"."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.PriorityLevelConfigurationCondition']"""
    conditions: core.optional[
        list[io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationCondition]
    ]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_Subject:
    """Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.GroupSubject', 'io.k8s.api.flowcontrol.v1beta3.ServiceAccountSubject', 'io.k8s.api.flowcontrol.v1beta3.UserSubject']"""
    group: core.optional[io_k8s_api_flowcontrol_v1beta3_GroupSubject]
    kind: str
    serviceAccount: core.optional[io_k8s_api_flowcontrol_v1beta3_ServiceAccountSubject]
    user: core.optional[io_k8s_api_flowcontrol_v1beta3_UserSubject]


@core.schema
class io_k8s_api_networking_v1_IngressLoadBalancerIngress:
    """IngressLoadBalancerIngress represents the status of a load-balancer ingress point."""

    """Dependencies: ['io.k8s.api.networking.v1.IngressPortStatus']"""
    hostname: core.optional[str]
    ip: core.optional[str]
    ports: core.optional[list[io_k8s_api_networking_v1_IngressPortStatus]]


@core.schema
class io_k8s_api_networking_v1_IngressLoadBalancerStatus:
    """IngressLoadBalancerStatus represents the status of a load-balancer."""

    """Dependencies: ['io.k8s.api.networking.v1.IngressLoadBalancerIngress']"""
    ingress: core.optional[list[io_k8s_api_networking_v1_IngressLoadBalancerIngress]]


@core.schema
class io_k8s_api_networking_v1_IngressServiceBackend:
    """IngressServiceBackend references a Kubernetes Service as a Backend."""

    """Dependencies: ['io.k8s.api.networking.v1.ServiceBackendPort']"""
    name: str
    port: core.optional[io_k8s_api_networking_v1_ServiceBackendPort]


@core.schema
class io_k8s_api_networking_v1_IngressStatus:
    """IngressStatus describe the current state of the Ingress."""

    """Dependencies: ['io.k8s.api.networking.v1.IngressLoadBalancerStatus']"""
    loadBalancer: core.optional[io_k8s_api_networking_v1_IngressLoadBalancerStatus]


@core.schema
class io_k8s_api_networking_v1_NetworkPolicyPort:
    """NetworkPolicyPort describes a port to allow traffic on"""

    """Dependencies: ['io.k8s.apimachinery.pkg.util.intstr.IntOrString']"""
    endPort: core.optional[int]
    port: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]
    protocol: core.optional[str]


@core.schema
class io_k8s_api_networking_v1alpha1_IPAddressSpec:
    """IPAddressSpec describe the attributes in an IP Address."""

    """Dependencies: ['io.k8s.api.networking.v1alpha1.ParentReference']"""
    parentRef: io_k8s_api_networking_v1alpha1_ParentReference


@core.schema
class io_k8s_api_resource_v1alpha2_DriverAllocationResult:
    """DriverAllocationResult contains vendor parameters and the allocation result for one request."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.NamedResourcesAllocationResult', 'io.k8s.apimachinery.pkg.runtime.RawExtension']"""
    namedResources: core.optional[
        io_k8s_api_resource_v1alpha2_NamedResourcesAllocationResult
    ]
    vendorRequestParameters: core.optional[io_k8s_apimachinery_pkg_runtime_RawExtension]


@core.schema
class io_k8s_api_resource_v1alpha2_NamedResourcesAttribute:
    """NamedResourcesAttribute is a combination of an attribute name and its value."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.NamedResourcesIntSlice', 'io.k8s.apimachinery.pkg.api.resource.Quantity', 'io.k8s.api.resource.v1alpha2.NamedResourcesStringSlice']"""
    bool: core.optional[bool]
    int: core.optional[int]
    intSlice: core.optional[io_k8s_api_resource_v1alpha2_NamedResourcesIntSlice]
    name: str
    quantity: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]
    string: core.optional[str]
    stringSlice: core.optional[io_k8s_api_resource_v1alpha2_NamedResourcesStringSlice]
    version: core.optional[str]


@core.schema
class io_k8s_api_resource_v1alpha2_NamedResourcesInstance:
    """NamedResourcesInstance represents one individual hardware instance that can be selected based on its attributes."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.NamedResourcesAttribute']"""
    attributes: core.optional[
        list[io_k8s_api_resource_v1alpha2_NamedResourcesAttribute]
    ]
    name: str


@core.schema
class io_k8s_api_resource_v1alpha2_NamedResourcesResources:
    """NamedResourcesResources is used in ResourceModel."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.NamedResourcesInstance']"""
    instances: list[io_k8s_api_resource_v1alpha2_NamedResourcesInstance]


@core.schema
class io_k8s_api_resource_v1alpha2_PodSchedulingContextStatus:
    """PodSchedulingContextStatus describes where resources for the Pod can be allocated."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceClaimSchedulingStatus']"""
    resourceClaims: core.optional[
        list[io_k8s_api_resource_v1alpha2_ResourceClaimSchedulingStatus]
    ]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceRequest:
    """ResourceRequest is a request for resources from one particular driver."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.NamedResourcesRequest', 'io.k8s.apimachinery.pkg.runtime.RawExtension']"""
    namedResources: core.optional[io_k8s_api_resource_v1alpha2_NamedResourcesRequest]
    vendorParameters: core.optional[io_k8s_apimachinery_pkg_runtime_RawExtension]


@core.schema
class io_k8s_api_resource_v1alpha2_StructuredResourceHandle:
    """StructuredResourceHandle is the in-tree representation of the allocation result."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.DriverAllocationResult', 'io.k8s.apimachinery.pkg.runtime.RawExtension', 'io.k8s.apimachinery.pkg.runtime.RawExtension']"""
    nodeName: core.optional[str]
    results: list[io_k8s_api_resource_v1alpha2_DriverAllocationResult]
    vendorClaimParameters: core.optional[io_k8s_apimachinery_pkg_runtime_RawExtension]
    vendorClassParameters: core.optional[io_k8s_apimachinery_pkg_runtime_RawExtension]


@core.schema
class io_k8s_api_resource_v1alpha2_VendorParameters:
    """VendorParameters are opaque parameters for one particular driver."""

    """Dependencies: ['io.k8s.apimachinery.pkg.runtime.RawExtension']"""
    driverName: core.optional[str]
    parameters: core.optional[io_k8s_apimachinery_pkg_runtime_RawExtension]


@core.schema
class io_k8s_api_storage_v1_CSIDriverSpec:
    """CSIDriverSpec is the specification of a CSIDriver."""

    """Dependencies: ['io.k8s.api.storage.v1.TokenRequest']"""
    attachRequired: core.optional[bool]
    fsGroupPolicy: core.optional[str]
    podInfoOnMount: core.optional[bool]
    requiresRepublish: core.optional[bool]
    seLinuxMount: core.optional[bool]
    storageCapacity: core.optional[bool]
    tokenRequests: core.optional[list[io_k8s_api_storage_v1_TokenRequest]]
    volumeLifecycleModes: core.optional[list[str]]


@core.schema
class io_k8s_api_storage_v1_CSINodeDriver:
    """CSINodeDriver holds information about the specification of one CSI driver installed on a node"""

    """Dependencies: ['io.k8s.api.storage.v1.VolumeNodeResources']"""
    allocatable: core.optional[io_k8s_api_storage_v1_VolumeNodeResources]
    name: str
    nodeID: str
    topologyKeys: core.optional[list[str]]


@core.schema
class io_k8s_api_storage_v1_CSINodeSpec:
    """CSINodeSpec holds information about the specification of all CSI drivers installed on a node"""

    """Dependencies: ['io.k8s.api.storage.v1.CSINodeDriver']"""
    drivers: list[io_k8s_api_storage_v1_CSINodeDriver]


@core.schema
class io_k8s_api_storage_v1_VolumeError:
    """VolumeError captures an error encountered during a volume operation."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    message: core.optional[str]
    time: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]


@core.schema
class io_k8s_api_storagemigration_v1alpha1_MigrationCondition:
    """Describes the state of a migration at a certain point."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastUpdateTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_api_storagemigration_v1alpha1_StorageVersionMigrationStatus:
    """Status of the storage version migration."""

    """Dependencies: ['io.k8s.api.storagemigration.v1alpha1.MigrationCondition']"""
    conditions: core.optional[
        list[io_k8s_api_storagemigration_v1alpha1_MigrationCondition]
    ]
    resourceVersion: core.optional[str]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceConversion:
    """CustomResourceConversion describes how to convert different versions of a CR."""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.WebhookConversion']"""
    strategy: str
    webhook: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_WebhookConversion
    ]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionCondition:
    """CustomResourceDefinitionCondition contains details for the current condition of this pod."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    reason: core.optional[str]
    status: str
    type: str


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionStatus:
    """CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition"""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionNames', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionCondition']"""
    acceptedNames: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionNames
    ]
    conditions: core.optional[
        list[
            io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionCondition
        ]
    ]
    storedVersions: core.optional[list[str]]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionVersion:
    """CustomResourceDefinitionVersion describes a version for CRD."""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceColumnDefinition', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceValidation', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.SelectableField', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceSubresources']"""
    additionalPrinterColumns: core.optional[
        list[
            io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceColumnDefinition
        ]
    ]
    deprecated: core.optional[bool]
    deprecationWarning: core.optional[str]
    name: str
    schema: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceValidation
    ]
    selectableFields: core.optional[
        list[io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_SelectableField]
    ]
    served: bool
    storage: bool
    subresources: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceSubresources
    ]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_APIGroup:
    """APIGroup contains the name, the supported versions, and the preferred version of a group."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.GroupVersionForDiscovery', 'io.k8s.apimachinery.pkg.apis.meta.v1.ServerAddressByClientCIDR', 'io.k8s.apimachinery.pkg.apis.meta.v1.GroupVersionForDiscovery']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    name: str
    preferredVersion: core.optional[
        io_k8s_apimachinery_pkg_apis_meta_v1_GroupVersionForDiscovery
    ]
    serverAddressByClientCIDRs: core.optional[
        list[io_k8s_apimachinery_pkg_apis_meta_v1_ServerAddressByClientCIDR]
    ]
    versions: list[io_k8s_apimachinery_pkg_apis_meta_v1_GroupVersionForDiscovery]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_APIGroupList:
    """APIGroupList is a list of APIGroup, to allow clients to discover the API at /apis."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.APIGroup']"""
    apiVersion: core.optional[str]
    groups: list[io_k8s_apimachinery_pkg_apis_meta_v1_APIGroup]
    kind: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_APIVersions:
    """APIVersions lists the versions that are available, to allow clients to discover the API at /api, which is the root path of the legacy v1 API."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ServerAddressByClientCIDR']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    serverAddressByClientCIDRs: list[
        io_k8s_apimachinery_pkg_apis_meta_v1_ServerAddressByClientCIDR
    ]
    versions: list[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_Condition:
    """Condition contains details for one aspect of the current state of this API Resource."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    lastTransitionTime: io_k8s_apimachinery_pkg_apis_meta_v1_Time
    message: str
    observedGeneration: core.optional[int]
    reason: str
    status: str
    type: str


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_DeleteOptions:
    """DeleteOptions may be provided when deleting an API object."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Preconditions']"""
    apiVersion: core.optional[str]
    dryRun: core.optional[list[str]]
    gracePeriodSeconds: core.optional[int]
    kind: core.optional[str]
    orphanDependents: core.optional[bool]
    preconditions: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Preconditions]
    propagationPolicy: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector:
    """A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelectorRequirement']"""
    matchExpressions: core.optional[
        list[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelectorRequirement]
    ]
    matchLabels: core.optional[dict[str, str]]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_ManagedFieldsEntry:
    """ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.FieldsV1', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    apiVersion: core.optional[str]
    fieldsType: core.optional[str]
    fieldsV1: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_FieldsV1]
    manager: core.optional[str]
    operation: core.optional[str]
    subresource: core.optional[str]
    time: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta:
    """ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.ManagedFieldsEntry', 'io.k8s.apimachinery.pkg.apis.meta.v1.OwnerReference']"""
    annotations: core.optional[dict[str, str]]
    creationTimestamp: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    deletionGracePeriodSeconds: core.optional[int]
    deletionTimestamp: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    finalizers: core.optional[list[str]]
    generateName: core.optional[str]
    generation: core.optional[int]
    labels: core.optional[dict[str, str]]
    managedFields: core.optional[
        list[io_k8s_apimachinery_pkg_apis_meta_v1_ManagedFieldsEntry]
    ]
    name: core.optional[str]
    namespace: core.optional[str]
    ownerReferences: core.optional[
        list[io_k8s_apimachinery_pkg_apis_meta_v1_OwnerReference]
    ]
    resourceVersion: core.optional[str]
    selfLink: core.optional[str]
    uid: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_Status:
    """Status is a return value for calls that don't return other objects."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.StatusDetails', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    code: core.optional[int]
    details: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_StatusDetails]
    kind: core.optional[str]
    message: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]
    reason: core.optional[str]
    status: core.optional[str]


@core.schema
class io_k8s_apimachinery_pkg_apis_meta_v1_WatchEvent:
    """Event represents a single event to a watched resource."""

    """Dependencies: ['io.k8s.apimachinery.pkg.runtime.RawExtension']"""
    object: io_k8s_apimachinery_pkg_runtime_RawExtension
    type: str


@core.schema
class io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIServiceSpec:
    """APIServiceSpec contains information for locating and communicating with a server. Only https is supported, though you are able to disable certificate verification."""

    """Dependencies: ['io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.ServiceReference']"""
    caBundle: core.optional[str]
    group: core.optional[str]
    groupPriorityMinimum: int
    insecureSkipTLSVerify: core.optional[bool]
    service: core.optional[
        io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_ServiceReference
    ]
    version: core.optional[str]
    versionPriority: int


@core.schema
class io_k8s_api_admissionregistration_v1_MatchResources:
    """MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)"""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.NamedRuleWithOperations', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.admissionregistration.v1.NamedRuleWithOperations']"""
    excludeResourceRules: core.optional[
        list[io_k8s_api_admissionregistration_v1_NamedRuleWithOperations]
    ]
    matchPolicy: core.optional[str]
    namespaceSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    objectSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    resourceRules: core.optional[
        list[io_k8s_api_admissionregistration_v1_NamedRuleWithOperations]
    ]


@core.schema
class io_k8s_api_admissionregistration_v1_MutatingWebhook:
    """MutatingWebhook describes an admission webhook and the resources and operations it applies to."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.WebhookClientConfig', 'io.k8s.api.admissionregistration.v1.MatchCondition', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.admissionregistration.v1.RuleWithOperations']"""
    admissionReviewVersions: list[str]
    clientConfig: io_k8s_api_admissionregistration_v1_WebhookClientConfig
    failurePolicy: core.optional[str]
    matchConditions: core.optional[
        list[io_k8s_api_admissionregistration_v1_MatchCondition]
    ]
    matchPolicy: core.optional[str]
    name: str
    namespaceSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    objectSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    reinvocationPolicy: core.optional[str]
    rules: core.optional[list[io_k8s_api_admissionregistration_v1_RuleWithOperations]]
    sideEffects: str
    timeoutSeconds: core.optional[int]


@core.schema
class io_k8s_api_admissionregistration_v1_MutatingWebhookConfiguration:
    """MutatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and may change the object."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.admissionregistration.v1.MutatingWebhook']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    webhooks: core.optional[list[io_k8s_api_admissionregistration_v1_MutatingWebhook]]


@core.schema
class io_k8s_api_admissionregistration_v1_MutatingWebhookConfigurationList:
    """MutatingWebhookConfigurationList is a list of MutatingWebhookConfiguration."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.MutatingWebhookConfiguration', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_admissionregistration_v1_MutatingWebhookConfiguration]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_admissionregistration_v1_ParamRef:
    """ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    name: core.optional[str]
    namespace: core.optional[str]
    parameterNotFoundAction: core.optional[str]
    selector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicyBindingSpec:
    """ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.MatchResources', 'io.k8s.api.admissionregistration.v1.ParamRef']"""
    matchResources: core.optional[io_k8s_api_admissionregistration_v1_MatchResources]
    paramRef: core.optional[io_k8s_api_admissionregistration_v1_ParamRef]
    policyName: core.optional[str]
    validationActions: core.optional[list[str]]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicySpec:
    """ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.AuditAnnotation', 'io.k8s.api.admissionregistration.v1.MatchCondition', 'io.k8s.api.admissionregistration.v1.MatchResources', 'io.k8s.api.admissionregistration.v1.ParamKind', 'io.k8s.api.admissionregistration.v1.Validation', 'io.k8s.api.admissionregistration.v1.Variable']"""
    auditAnnotations: core.optional[
        list[io_k8s_api_admissionregistration_v1_AuditAnnotation]
    ]
    failurePolicy: core.optional[str]
    matchConditions: core.optional[
        list[io_k8s_api_admissionregistration_v1_MatchCondition]
    ]
    matchConstraints: core.optional[io_k8s_api_admissionregistration_v1_MatchResources]
    paramKind: core.optional[io_k8s_api_admissionregistration_v1_ParamKind]
    validations: core.optional[list[io_k8s_api_admissionregistration_v1_Validation]]
    variables: core.optional[list[io_k8s_api_admissionregistration_v1_Variable]]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicyStatus:
    """ValidatingAdmissionPolicyStatus represents the status of an admission validation policy."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Condition', 'io.k8s.api.admissionregistration.v1.TypeChecking']"""
    conditions: core.optional[list[io_k8s_apimachinery_pkg_apis_meta_v1_Condition]]
    observedGeneration: core.optional[int]
    typeChecking: core.optional[io_k8s_api_admissionregistration_v1_TypeChecking]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingWebhook:
    """ValidatingWebhook describes an admission webhook and the resources and operations it applies to."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.WebhookClientConfig', 'io.k8s.api.admissionregistration.v1.MatchCondition', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.admissionregistration.v1.RuleWithOperations']"""
    admissionReviewVersions: list[str]
    clientConfig: io_k8s_api_admissionregistration_v1_WebhookClientConfig
    failurePolicy: core.optional[str]
    matchConditions: core.optional[
        list[io_k8s_api_admissionregistration_v1_MatchCondition]
    ]
    matchPolicy: core.optional[str]
    name: str
    namespaceSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    objectSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    rules: core.optional[list[io_k8s_api_admissionregistration_v1_RuleWithOperations]]
    sideEffects: str
    timeoutSeconds: core.optional[int]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingWebhookConfiguration:
    """ValidatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and object without changing it."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.admissionregistration.v1.ValidatingWebhook']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    webhooks: core.optional[list[io_k8s_api_admissionregistration_v1_ValidatingWebhook]]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingWebhookConfigurationList:
    """ValidatingWebhookConfigurationList is a list of ValidatingWebhookConfiguration."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.ValidatingWebhookConfiguration', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_admissionregistration_v1_ValidatingWebhookConfiguration]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_MatchResources:
    """MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)"""

    """Dependencies: ['io.k8s.api.admissionregistration.v1alpha1.NamedRuleWithOperations', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.admissionregistration.v1alpha1.NamedRuleWithOperations']"""
    excludeResourceRules: core.optional[
        list[io_k8s_api_admissionregistration_v1alpha1_NamedRuleWithOperations]
    ]
    matchPolicy: core.optional[str]
    namespaceSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    objectSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    resourceRules: core.optional[
        list[io_k8s_api_admissionregistration_v1alpha1_NamedRuleWithOperations]
    ]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ParamRef:
    """ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    name: core.optional[str]
    namespace: core.optional[str]
    parameterNotFoundAction: core.optional[str]
    selector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicyBindingSpec:
    """ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1alpha1.MatchResources', 'io.k8s.api.admissionregistration.v1alpha1.ParamRef']"""
    matchResources: core.optional[
        io_k8s_api_admissionregistration_v1alpha1_MatchResources
    ]
    paramRef: core.optional[io_k8s_api_admissionregistration_v1alpha1_ParamRef]
    policyName: core.optional[str]
    validationActions: core.optional[list[str]]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicySpec:
    """ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1alpha1.AuditAnnotation', 'io.k8s.api.admissionregistration.v1alpha1.MatchCondition', 'io.k8s.api.admissionregistration.v1alpha1.MatchResources', 'io.k8s.api.admissionregistration.v1alpha1.ParamKind', 'io.k8s.api.admissionregistration.v1alpha1.Validation', 'io.k8s.api.admissionregistration.v1alpha1.Variable']"""
    auditAnnotations: core.optional[
        list[io_k8s_api_admissionregistration_v1alpha1_AuditAnnotation]
    ]
    failurePolicy: core.optional[str]
    matchConditions: core.optional[
        list[io_k8s_api_admissionregistration_v1alpha1_MatchCondition]
    ]
    matchConstraints: core.optional[
        io_k8s_api_admissionregistration_v1alpha1_MatchResources
    ]
    paramKind: core.optional[io_k8s_api_admissionregistration_v1alpha1_ParamKind]
    validations: core.optional[
        list[io_k8s_api_admissionregistration_v1alpha1_Validation]
    ]
    variables: core.optional[list[io_k8s_api_admissionregistration_v1alpha1_Variable]]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicyStatus:
    """ValidatingAdmissionPolicyStatus represents the status of a ValidatingAdmissionPolicy."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Condition', 'io.k8s.api.admissionregistration.v1alpha1.TypeChecking']"""
    conditions: core.optional[list[io_k8s_apimachinery_pkg_apis_meta_v1_Condition]]
    observedGeneration: core.optional[int]
    typeChecking: core.optional[io_k8s_api_admissionregistration_v1alpha1_TypeChecking]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_MatchResources:
    """MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)"""

    """Dependencies: ['io.k8s.api.admissionregistration.v1beta1.NamedRuleWithOperations', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.admissionregistration.v1beta1.NamedRuleWithOperations']"""
    excludeResourceRules: core.optional[
        list[io_k8s_api_admissionregistration_v1beta1_NamedRuleWithOperations]
    ]
    matchPolicy: core.optional[str]
    namespaceSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    objectSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    resourceRules: core.optional[
        list[io_k8s_api_admissionregistration_v1beta1_NamedRuleWithOperations]
    ]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ParamRef:
    """ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    name: core.optional[str]
    namespace: core.optional[str]
    parameterNotFoundAction: core.optional[str]
    selector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicyBindingSpec:
    """ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1beta1.MatchResources', 'io.k8s.api.admissionregistration.v1beta1.ParamRef']"""
    matchResources: core.optional[
        io_k8s_api_admissionregistration_v1beta1_MatchResources
    ]
    paramRef: core.optional[io_k8s_api_admissionregistration_v1beta1_ParamRef]
    policyName: core.optional[str]
    validationActions: core.optional[list[str]]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicySpec:
    """ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1beta1.AuditAnnotation', 'io.k8s.api.admissionregistration.v1beta1.MatchCondition', 'io.k8s.api.admissionregistration.v1beta1.MatchResources', 'io.k8s.api.admissionregistration.v1beta1.ParamKind', 'io.k8s.api.admissionregistration.v1beta1.Validation', 'io.k8s.api.admissionregistration.v1beta1.Variable']"""
    auditAnnotations: core.optional[
        list[io_k8s_api_admissionregistration_v1beta1_AuditAnnotation]
    ]
    failurePolicy: core.optional[str]
    matchConditions: core.optional[
        list[io_k8s_api_admissionregistration_v1beta1_MatchCondition]
    ]
    matchConstraints: core.optional[
        io_k8s_api_admissionregistration_v1beta1_MatchResources
    ]
    paramKind: core.optional[io_k8s_api_admissionregistration_v1beta1_ParamKind]
    validations: core.optional[
        list[io_k8s_api_admissionregistration_v1beta1_Validation]
    ]
    variables: core.optional[list[io_k8s_api_admissionregistration_v1beta1_Variable]]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicyStatus:
    """ValidatingAdmissionPolicyStatus represents the status of an admission validation policy."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Condition', 'io.k8s.api.admissionregistration.v1beta1.TypeChecking']"""
    conditions: core.optional[list[io_k8s_apimachinery_pkg_apis_meta_v1_Condition]]
    observedGeneration: core.optional[int]
    typeChecking: core.optional[io_k8s_api_admissionregistration_v1beta1_TypeChecking]


@core.schema
class io_k8s_api_apiserverinternal_v1alpha1_StorageVersion:
    """Storage version of a specific resource."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.apiserverinternal.v1alpha1.StorageVersionSpec', 'io.k8s.api.apiserverinternal.v1alpha1.StorageVersionStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_apiserverinternal_v1alpha1_StorageVersionSpec
    status: io_k8s_api_apiserverinternal_v1alpha1_StorageVersionStatus


@core.schema
class io_k8s_api_apiserverinternal_v1alpha1_StorageVersionList:
    """A list of StorageVersions."""

    """Dependencies: ['io.k8s.api.apiserverinternal.v1alpha1.StorageVersion', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_apiserverinternal_v1alpha1_StorageVersion]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_apps_v1_ControllerRevision:
    """ControllerRevision implements an immutable snapshot of state data. Clients are responsible for serializing and deserializing the objects that contain their internal state. Once a ControllerRevision has been successfully created, it can not be updated. The API Server will fail validation of all requests that attempt to mutate the Data field. ControllerRevisions may, however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet controllers for update and rollback, this object is beta. However, it may be subject to name and representation changes in future releases, and clients should not depend on its stability. It is primarily for internal use by controllers."""

    """Dependencies: ['io.k8s.apimachinery.pkg.runtime.RawExtension', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    apiVersion: core.optional[str]
    data: core.optional[io_k8s_apimachinery_pkg_runtime_RawExtension]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    revision: int


@core.schema
class io_k8s_api_apps_v1_ControllerRevisionList:
    """ControllerRevisionList is a resource containing a list of ControllerRevision objects."""

    """Dependencies: ['io.k8s.api.apps.v1.ControllerRevision', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_apps_v1_ControllerRevision]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_apps_v1_DaemonSetUpdateStrategy:
    """DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet."""

    """Dependencies: ['io.k8s.api.apps.v1.RollingUpdateDaemonSet']"""
    rollingUpdate: core.optional[io_k8s_api_apps_v1_RollingUpdateDaemonSet]
    type: core.optional[str]


@core.schema
class io_k8s_api_apps_v1_DeploymentStrategy:
    """DeploymentStrategy describes how to replace existing pods with new ones."""

    """Dependencies: ['io.k8s.api.apps.v1.RollingUpdateDeployment']"""
    rollingUpdate: core.optional[io_k8s_api_apps_v1_RollingUpdateDeployment]
    type: core.optional[str]


@core.schema
class io_k8s_api_authentication_v1_SelfSubjectReview:
    """SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated.  If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authentication.v1.SelfSubjectReviewStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    status: core.optional[io_k8s_api_authentication_v1_SelfSubjectReviewStatus]


@core.schema
class io_k8s_api_authentication_v1_TokenRequest:
    """TokenRequest requests a token for a given service account."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authentication.v1.TokenRequestSpec', 'io.k8s.api.authentication.v1.TokenRequestStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_authentication_v1_TokenRequestSpec
    status: core.optional[io_k8s_api_authentication_v1_TokenRequestStatus]


@core.schema
class io_k8s_api_authentication_v1_TokenReview:
    """TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached by the webhook token authenticator plugin in the kube-apiserver."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authentication.v1.TokenReviewSpec', 'io.k8s.api.authentication.v1.TokenReviewStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_authentication_v1_TokenReviewSpec
    status: core.optional[io_k8s_api_authentication_v1_TokenReviewStatus]


@core.schema
class io_k8s_api_authentication_v1alpha1_SelfSubjectReview:
    """SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated.  If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authentication.v1alpha1.SelfSubjectReviewStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    status: core.optional[io_k8s_api_authentication_v1alpha1_SelfSubjectReviewStatus]


@core.schema
class io_k8s_api_authentication_v1beta1_SelfSubjectReview:
    """SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated.  If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authentication.v1beta1.SelfSubjectReviewStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    status: core.optional[io_k8s_api_authentication_v1beta1_SelfSubjectReviewStatus]


@core.schema
class io_k8s_api_authorization_v1_LocalSubjectAccessReview:
    """LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped policy that includes permissions checking."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authorization.v1.SubjectAccessReviewSpec', 'io.k8s.api.authorization.v1.SubjectAccessReviewStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_authorization_v1_SubjectAccessReviewSpec
    status: core.optional[io_k8s_api_authorization_v1_SubjectAccessReviewStatus]


@core.schema
class io_k8s_api_authorization_v1_SelfSubjectAccessReview:
    """SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling in a spec.namespace means "in all namespaces".  Self is a special case, because users should always be able to check whether they can perform an action"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authorization.v1.SelfSubjectAccessReviewSpec', 'io.k8s.api.authorization.v1.SubjectAccessReviewStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_authorization_v1_SelfSubjectAccessReviewSpec
    status: core.optional[io_k8s_api_authorization_v1_SubjectAccessReviewStatus]


@core.schema
class io_k8s_api_authorization_v1_SelfSubjectRulesReview:
    """SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace. The returned list of actions may be incomplete depending on the server's authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide actions, or to quickly let an end user reason about their permissions. It should NOT Be used by external systems to drive authorization decisions as this raises confused deputy, cache lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions to the API server."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authorization.v1.SelfSubjectRulesReviewSpec', 'io.k8s.api.authorization.v1.SubjectRulesReviewStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_authorization_v1_SelfSubjectRulesReviewSpec
    status: core.optional[io_k8s_api_authorization_v1_SubjectRulesReviewStatus]


@core.schema
class io_k8s_api_authorization_v1_SubjectAccessReview:
    """SubjectAccessReview checks whether or not a user or group can perform an action."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.authorization.v1.SubjectAccessReviewSpec', 'io.k8s.api.authorization.v1.SubjectAccessReviewStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_authorization_v1_SubjectAccessReviewSpec
    status: core.optional[io_k8s_api_authorization_v1_SubjectAccessReviewStatus]


@core.schema
class io_k8s_api_autoscaling_v1_HorizontalPodAutoscaler:
    """configuration of a horizontal pod autoscaler."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.autoscaling.v1.HorizontalPodAutoscalerSpec', 'io.k8s.api.autoscaling.v1.HorizontalPodAutoscalerStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_autoscaling_v1_HorizontalPodAutoscalerSpec]
    status: core.optional[io_k8s_api_autoscaling_v1_HorizontalPodAutoscalerStatus]


@core.schema
class io_k8s_api_autoscaling_v1_HorizontalPodAutoscalerList:
    """list of horizontal pod autoscaler objects."""

    """Dependencies: ['io.k8s.api.autoscaling.v1.HorizontalPodAutoscaler', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_autoscaling_v1_HorizontalPodAutoscaler]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_autoscaling_v1_Scale:
    """Scale represents a scaling request for a resource."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.autoscaling.v1.ScaleSpec', 'io.k8s.api.autoscaling.v1.ScaleStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_autoscaling_v1_ScaleSpec]
    status: core.optional[io_k8s_api_autoscaling_v1_ScaleStatus]


@core.schema
class io_k8s_api_autoscaling_v2_ContainerResourceMetricSource:
    """ContainerResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values will be averaged together before being compared to the target.  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.  Only one "target" type should be set."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricTarget']"""
    container: str
    name: str
    target: io_k8s_api_autoscaling_v2_MetricTarget


@core.schema
class io_k8s_api_autoscaling_v2_ContainerResourceMetricStatus:
    """ContainerResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing a single container in each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricValueStatus']"""
    container: str
    current: io_k8s_api_autoscaling_v2_MetricValueStatus
    name: str


@core.schema
class io_k8s_api_autoscaling_v2_MetricIdentifier:
    """MetricIdentifier defines the name and optionally selector for a metric"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    name: str
    selector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]


@core.schema
class io_k8s_api_autoscaling_v2_ObjectMetricSource:
    """ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object)."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.CrossVersionObjectReference', 'io.k8s.api.autoscaling.v2.MetricIdentifier', 'io.k8s.api.autoscaling.v2.MetricTarget']"""
    describedObject: io_k8s_api_autoscaling_v2_CrossVersionObjectReference
    metric: io_k8s_api_autoscaling_v2_MetricIdentifier
    target: io_k8s_api_autoscaling_v2_MetricTarget


@core.schema
class io_k8s_api_autoscaling_v2_ObjectMetricStatus:
    """ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object)."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricValueStatus', 'io.k8s.api.autoscaling.v2.CrossVersionObjectReference', 'io.k8s.api.autoscaling.v2.MetricIdentifier']"""
    current: io_k8s_api_autoscaling_v2_MetricValueStatus
    describedObject: io_k8s_api_autoscaling_v2_CrossVersionObjectReference
    metric: io_k8s_api_autoscaling_v2_MetricIdentifier


@core.schema
class io_k8s_api_autoscaling_v2_PodsMetricSource:
    """PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricIdentifier', 'io.k8s.api.autoscaling.v2.MetricTarget']"""
    metric: io_k8s_api_autoscaling_v2_MetricIdentifier
    target: io_k8s_api_autoscaling_v2_MetricTarget


@core.schema
class io_k8s_api_autoscaling_v2_PodsMetricStatus:
    """PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second)."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricValueStatus', 'io.k8s.api.autoscaling.v2.MetricIdentifier']"""
    current: io_k8s_api_autoscaling_v2_MetricValueStatus
    metric: io_k8s_api_autoscaling_v2_MetricIdentifier


@core.schema
class io_k8s_api_certificates_v1_CertificateSigningRequest:
    """CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a certificate signing request, and having it asynchronously approved and issued.

    Kubelets use this API to obtain:
     1. client certificates to authenticate to kube-apiserver (with the "kubernetes.io/kube-apiserver-client-kubelet" signerName).
     2. serving certificates for TLS endpoints kube-apiserver can connect to securely (with the "kubernetes.io/kubelet-serving" signerName).

    This API can be used to request client certificates to authenticate to kube-apiserver (with the "kubernetes.io/kube-apiserver-client" signerName), or to obtain certificates from custom non-Kubernetes signers.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.certificates.v1.CertificateSigningRequestSpec', 'io.k8s.api.certificates.v1.CertificateSigningRequestStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_certificates_v1_CertificateSigningRequestSpec
    status: core.optional[io_k8s_api_certificates_v1_CertificateSigningRequestStatus]


@core.schema
class io_k8s_api_certificates_v1_CertificateSigningRequestList:
    """CertificateSigningRequestList is a collection of CertificateSigningRequest objects"""

    """Dependencies: ['io.k8s.api.certificates.v1.CertificateSigningRequest', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_certificates_v1_CertificateSigningRequest]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_certificates_v1alpha1_ClusterTrustBundle:
    """ClusterTrustBundle is a cluster-scoped container for X.509 trust anchors (root certificates).

    ClusterTrustBundle objects are considered to be readable by any authenticated user in the cluster, because they can be mounted by pods using the `clusterTrustBundle` projection.  All service accounts have read access to ClusterTrustBundles by default.  Users who only have namespace-level access to a cluster can read ClusterTrustBundles by impersonating a serviceaccount that they have access to.

    It can be optionally associated with a particular assigner, in which case it contains one valid set of trust anchors for that signer. Signers may have multiple associated ClusterTrustBundles; each is an independent set of trust anchors for that signer. Admission control is used to enforce that only users with permissions on the signer can create or modify the corresponding bundle.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.certificates.v1alpha1.ClusterTrustBundleSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_certificates_v1alpha1_ClusterTrustBundleSpec


@core.schema
class io_k8s_api_certificates_v1alpha1_ClusterTrustBundleList:
    """ClusterTrustBundleList is a collection of ClusterTrustBundle objects"""

    """Dependencies: ['io.k8s.api.certificates.v1alpha1.ClusterTrustBundle', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_certificates_v1alpha1_ClusterTrustBundle]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_coordination_v1_Lease:
    """Lease defines a lease concept."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.coordination.v1.LeaseSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_coordination_v1_LeaseSpec]


@core.schema
class io_k8s_api_coordination_v1_LeaseList:
    """LeaseList is a list of Lease objects."""

    """Dependencies: ['io.k8s.api.coordination.v1.Lease', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_coordination_v1_Lease]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_Binding:
    """Binding ties one object to another; for example, a pod is bound to a node by a scheduler. Deprecated in 1.7, please use the bindings subresource of pods instead."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.ObjectReference']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    target: io_k8s_api_core_v1_ObjectReference


@core.schema
class io_k8s_api_core_v1_ClusterTrustBundleProjection:
    """ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    labelSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    name: core.optional[str]
    optional: core.optional[bool]
    path: str
    signerName: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ComponentStatus:
    """ComponentStatus (and ComponentStatusList) holds the cluster validation info. Deprecated: This API is deprecated in v1.19+"""

    """Dependencies: ['io.k8s.api.core.v1.ComponentCondition', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    apiVersion: core.optional[str]
    conditions: core.optional[list[io_k8s_api_core_v1_ComponentCondition]]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]


@core.schema
class io_k8s_api_core_v1_ComponentStatusList:
    """Status of all the conditions for the component as a list of ComponentStatus objects. Deprecated: This API is deprecated in v1.19+"""

    """Dependencies: ['io.k8s.api.core.v1.ComponentStatus', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_ComponentStatus]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_ConfigMap:
    """ConfigMap holds configuration data for pods to consume."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    apiVersion: core.optional[str]
    binaryData: core.optional[dict[str, str]]
    data: core.optional[dict[str, str]]
    immutable: core.optional[bool]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]


@core.schema
class io_k8s_api_core_v1_ConfigMapList:
    """ConfigMapList is a resource containing a list of ConfigMap objects."""

    """Dependencies: ['io.k8s.api.core.v1.ConfigMap', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_ConfigMap]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_ContainerState:
    """ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting."""

    """Dependencies: ['io.k8s.api.core.v1.ContainerStateRunning', 'io.k8s.api.core.v1.ContainerStateTerminated', 'io.k8s.api.core.v1.ContainerStateWaiting']"""
    running: core.optional[io_k8s_api_core_v1_ContainerStateRunning]
    terminated: core.optional[io_k8s_api_core_v1_ContainerStateTerminated]
    waiting: core.optional[io_k8s_api_core_v1_ContainerStateWaiting]


@core.schema
class io_k8s_api_core_v1_ContainerStatus:
    """ContainerStatus contains details for the current status of this container."""

    """Dependencies: ['io.k8s.api.core.v1.ContainerState', 'io.k8s.api.core.v1.ResourceRequirements', 'io.k8s.api.core.v1.ContainerState', 'io.k8s.api.core.v1.ContainerUser', 'io.k8s.api.core.v1.VolumeMountStatus']"""
    allocatedResources: core.optional[dict[str, str]]
    containerID: core.optional[str]
    image: str
    imageID: str
    lastState: core.optional[io_k8s_api_core_v1_ContainerState]
    name: str
    ready: bool
    resources: core.optional[io_k8s_api_core_v1_ResourceRequirements]
    restartCount: int
    started: core.optional[bool]
    state: core.optional[io_k8s_api_core_v1_ContainerState]
    user: core.optional[io_k8s_api_core_v1_ContainerUser]
    volumeMounts: core.optional[list[io_k8s_api_core_v1_VolumeMountStatus]]


@core.schema
class io_k8s_api_core_v1_DownwardAPIVolumeFile:
    """DownwardAPIVolumeFile represents information to create the file containing the pod field"""

    """Dependencies: ['io.k8s.api.core.v1.ObjectFieldSelector', 'io.k8s.api.core.v1.ResourceFieldSelector']"""
    fieldRef: core.optional[io_k8s_api_core_v1_ObjectFieldSelector]
    mode: core.optional[int]
    path: str
    resourceFieldRef: core.optional[io_k8s_api_core_v1_ResourceFieldSelector]


@core.schema
class io_k8s_api_core_v1_DownwardAPIVolumeSource:
    """DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling."""

    """Dependencies: ['io.k8s.api.core.v1.DownwardAPIVolumeFile']"""
    defaultMode: core.optional[int]
    items: core.optional[list[io_k8s_api_core_v1_DownwardAPIVolumeFile]]


@core.schema
class io_k8s_api_core_v1_Endpoints:
    """Endpoints is a collection of endpoints that implement the actual service. Example:

     Name: "mysvc",
     Subsets: [
       {
         Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
         Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
       },
       {
         Addresses: [{"ip": "10.10.3.3"}],
         Ports: [{"name": "a", "port": 93}, {"name": "b", "port": 76}]
       },
    ]"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.EndpointSubset']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    subsets: core.optional[list[io_k8s_api_core_v1_EndpointSubset]]


@core.schema
class io_k8s_api_core_v1_EndpointsList:
    """EndpointsList is a list of endpoints."""

    """Dependencies: ['io.k8s.api.core.v1.Endpoints', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_Endpoints]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_EnvVarSource:
    """EnvVarSource represents a source for the value of an EnvVar."""

    """Dependencies: ['io.k8s.api.core.v1.ConfigMapKeySelector', 'io.k8s.api.core.v1.ObjectFieldSelector', 'io.k8s.api.core.v1.ResourceFieldSelector', 'io.k8s.api.core.v1.SecretKeySelector']"""
    configMapKeyRef: core.optional[io_k8s_api_core_v1_ConfigMapKeySelector]
    fieldRef: core.optional[io_k8s_api_core_v1_ObjectFieldSelector]
    resourceFieldRef: core.optional[io_k8s_api_core_v1_ResourceFieldSelector]
    secretKeyRef: core.optional[io_k8s_api_core_v1_SecretKeySelector]


@core.schema
class io_k8s_api_core_v1_Event:
    """Event is a report of an event somewhere in the cluster.  Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.api.core.v1.ObjectReference', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.ObjectReference', 'io.k8s.api.core.v1.EventSeries', 'io.k8s.api.core.v1.EventSource']"""
    action: core.optional[str]
    apiVersion: core.optional[str]
    count: core.optional[int]
    eventTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_MicroTime]
    firstTimestamp: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    involvedObject: io_k8s_api_core_v1_ObjectReference
    kind: core.optional[str]
    lastTimestamp: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    message: core.optional[str]
    metadata: io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta
    reason: core.optional[str]
    related: core.optional[io_k8s_api_core_v1_ObjectReference]
    reportingComponent: core.optional[str]
    reportingInstance: core.optional[str]
    series: core.optional[io_k8s_api_core_v1_EventSeries]
    source: core.optional[io_k8s_api_core_v1_EventSource]
    type: core.optional[str]


@core.schema
class io_k8s_api_core_v1_EventList:
    """EventList is a list of events."""

    """Dependencies: ['io.k8s.api.core.v1.Event', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_Event]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_LifecycleHandler:
    """LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified."""

    """Dependencies: ['io.k8s.api.core.v1.ExecAction', 'io.k8s.api.core.v1.HTTPGetAction', 'io.k8s.api.core.v1.SleepAction', 'io.k8s.api.core.v1.TCPSocketAction']"""
    exec: core.optional[io_k8s_api_core_v1_ExecAction]
    httpGet: core.optional[io_k8s_api_core_v1_HTTPGetAction]
    sleep: core.optional[io_k8s_api_core_v1_SleepAction]
    tcpSocket: core.optional[io_k8s_api_core_v1_TCPSocketAction]


@core.schema
class io_k8s_api_core_v1_LimitRange:
    """LimitRange sets resource usage limits for each kind of resource in a Namespace."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.LimitRangeSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_LimitRangeSpec]


@core.schema
class io_k8s_api_core_v1_LimitRangeList:
    """LimitRangeList is a list of LimitRange items."""

    """Dependencies: ['io.k8s.api.core.v1.LimitRange', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_LimitRange]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_Namespace:
    """Namespace provides a scope for Names. Use of multiple namespaces is optional."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.NamespaceSpec', 'io.k8s.api.core.v1.NamespaceStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_NamespaceSpec]
    status: core.optional[io_k8s_api_core_v1_NamespaceStatus]


@core.schema
class io_k8s_api_core_v1_NamespaceList:
    """NamespaceList is a list of Namespaces."""

    """Dependencies: ['io.k8s.api.core.v1.Namespace', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_Namespace]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_NodeAffinity:
    """Node affinity is a group of node affinity scheduling rules."""

    """Dependencies: ['io.k8s.api.core.v1.PreferredSchedulingTerm', 'io.k8s.api.core.v1.NodeSelector']"""
    preferredDuringSchedulingIgnoredDuringExecution: core.optional[
        list[io_k8s_api_core_v1_PreferredSchedulingTerm]
    ]
    requiredDuringSchedulingIgnoredDuringExecution: core.optional[
        io_k8s_api_core_v1_NodeSelector
    ]


@core.schema
class io_k8s_api_core_v1_NodeSpec:
    """NodeSpec describes the attributes that a node is created with."""

    """Dependencies: ['io.k8s.api.core.v1.NodeConfigSource', 'io.k8s.api.core.v1.Taint']"""
    configSource: core.optional[io_k8s_api_core_v1_NodeConfigSource]
    externalID: core.optional[str]
    podCIDR: core.optional[str]
    podCIDRs: core.optional[list[str]]
    providerID: core.optional[str]
    taints: core.optional[list[io_k8s_api_core_v1_Taint]]
    unschedulable: core.optional[bool]


@core.schema
class io_k8s_api_core_v1_PersistentVolumeClaimSpec:
    """PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes"""

    """Dependencies: ['io.k8s.api.core.v1.TypedLocalObjectReference', 'io.k8s.api.core.v1.TypedObjectReference', 'io.k8s.api.core.v1.VolumeResourceRequirements', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    accessModes: core.optional[list[str]]
    dataSource: core.optional[io_k8s_api_core_v1_TypedLocalObjectReference]
    dataSourceRef: core.optional[io_k8s_api_core_v1_TypedObjectReference]
    resources: core.optional[io_k8s_api_core_v1_VolumeResourceRequirements]
    selector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    storageClassName: core.optional[str]
    volumeAttributesClassName: core.optional[str]
    volumeMode: core.optional[str]
    volumeName: core.optional[str]


@core.schema
class io_k8s_api_core_v1_PersistentVolumeClaimTemplate:
    """PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.PersistentVolumeClaimSpec']"""
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_core_v1_PersistentVolumeClaimSpec


@core.schema
class io_k8s_api_core_v1_PersistentVolumeSpec:
    """PersistentVolumeSpec is the specification of a persistent volume."""

    """Dependencies: ['io.k8s.api.core.v1.AWSElasticBlockStoreVolumeSource', 'io.k8s.api.core.v1.AzureDiskVolumeSource', 'io.k8s.api.core.v1.AzureFilePersistentVolumeSource', 'io.k8s.api.core.v1.CephFSPersistentVolumeSource', 'io.k8s.api.core.v1.CinderPersistentVolumeSource', 'io.k8s.api.core.v1.ObjectReference', 'io.k8s.api.core.v1.CSIPersistentVolumeSource', 'io.k8s.api.core.v1.FCVolumeSource', 'io.k8s.api.core.v1.FlexPersistentVolumeSource', 'io.k8s.api.core.v1.FlockerVolumeSource', 'io.k8s.api.core.v1.GCEPersistentDiskVolumeSource', 'io.k8s.api.core.v1.GlusterfsPersistentVolumeSource', 'io.k8s.api.core.v1.HostPathVolumeSource', 'io.k8s.api.core.v1.ISCSIPersistentVolumeSource', 'io.k8s.api.core.v1.LocalVolumeSource', 'io.k8s.api.core.v1.NFSVolumeSource', 'io.k8s.api.core.v1.VolumeNodeAffinity', 'io.k8s.api.core.v1.PhotonPersistentDiskVolumeSource', 'io.k8s.api.core.v1.PortworxVolumeSource', 'io.k8s.api.core.v1.QuobyteVolumeSource', 'io.k8s.api.core.v1.RBDPersistentVolumeSource', 'io.k8s.api.core.v1.ScaleIOPersistentVolumeSource', 'io.k8s.api.core.v1.StorageOSPersistentVolumeSource', 'io.k8s.api.core.v1.VsphereVirtualDiskVolumeSource']"""
    accessModes: core.optional[list[str]]
    awsElasticBlockStore: core.optional[
        io_k8s_api_core_v1_AWSElasticBlockStoreVolumeSource
    ]
    azureDisk: core.optional[io_k8s_api_core_v1_AzureDiskVolumeSource]
    azureFile: core.optional[io_k8s_api_core_v1_AzureFilePersistentVolumeSource]
    capacity: core.optional[dict[str, str]]
    cephfs: core.optional[io_k8s_api_core_v1_CephFSPersistentVolumeSource]
    cinder: core.optional[io_k8s_api_core_v1_CinderPersistentVolumeSource]
    claimRef: core.optional[io_k8s_api_core_v1_ObjectReference]
    csi: core.optional[io_k8s_api_core_v1_CSIPersistentVolumeSource]
    fc: core.optional[io_k8s_api_core_v1_FCVolumeSource]
    flexVolume: core.optional[io_k8s_api_core_v1_FlexPersistentVolumeSource]
    flocker: core.optional[io_k8s_api_core_v1_FlockerVolumeSource]
    gcePersistentDisk: core.optional[io_k8s_api_core_v1_GCEPersistentDiskVolumeSource]
    glusterfs: core.optional[io_k8s_api_core_v1_GlusterfsPersistentVolumeSource]
    hostPath: core.optional[io_k8s_api_core_v1_HostPathVolumeSource]
    iscsi: core.optional[io_k8s_api_core_v1_ISCSIPersistentVolumeSource]
    local: core.optional[io_k8s_api_core_v1_LocalVolumeSource]
    mountOptions: core.optional[list[str]]
    nfs: core.optional[io_k8s_api_core_v1_NFSVolumeSource]
    nodeAffinity: core.optional[io_k8s_api_core_v1_VolumeNodeAffinity]
    persistentVolumeReclaimPolicy: core.optional[str]
    photonPersistentDisk: core.optional[
        io_k8s_api_core_v1_PhotonPersistentDiskVolumeSource
    ]
    portworxVolume: core.optional[io_k8s_api_core_v1_PortworxVolumeSource]
    quobyte: core.optional[io_k8s_api_core_v1_QuobyteVolumeSource]
    rbd: core.optional[io_k8s_api_core_v1_RBDPersistentVolumeSource]
    scaleIO: core.optional[io_k8s_api_core_v1_ScaleIOPersistentVolumeSource]
    storageClassName: core.optional[str]
    storageos: core.optional[io_k8s_api_core_v1_StorageOSPersistentVolumeSource]
    volumeAttributesClassName: core.optional[str]
    volumeMode: core.optional[str]
    vsphereVolume: core.optional[io_k8s_api_core_v1_VsphereVirtualDiskVolumeSource]


@core.schema
class io_k8s_api_core_v1_PodAffinityTerm:
    """Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    labelSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    matchLabelKeys: core.optional[list[str]]
    mismatchLabelKeys: core.optional[list[str]]
    namespaceSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    namespaces: core.optional[list[str]]
    topologyKey: str


@core.schema
class io_k8s_api_core_v1_PodStatus:
    """PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane."""

    """Dependencies: ['io.k8s.api.core.v1.PodCondition', 'io.k8s.api.core.v1.ContainerStatus', 'io.k8s.api.core.v1.ContainerStatus', 'io.k8s.api.core.v1.HostIP', 'io.k8s.api.core.v1.ContainerStatus', 'io.k8s.api.core.v1.PodIP', 'io.k8s.api.core.v1.PodResourceClaimStatus', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    conditions: core.optional[list[io_k8s_api_core_v1_PodCondition]]
    containerStatuses: core.optional[list[io_k8s_api_core_v1_ContainerStatus]]
    ephemeralContainerStatuses: core.optional[list[io_k8s_api_core_v1_ContainerStatus]]
    hostIP: core.optional[str]
    hostIPs: core.optional[list[io_k8s_api_core_v1_HostIP]]
    initContainerStatuses: core.optional[list[io_k8s_api_core_v1_ContainerStatus]]
    message: core.optional[str]
    nominatedNodeName: core.optional[str]
    phase: core.optional[str]
    podIP: core.optional[str]
    podIPs: core.optional[list[io_k8s_api_core_v1_PodIP]]
    qosClass: core.optional[str]
    reason: core.optional[str]
    resize: core.optional[str]
    resourceClaimStatuses: core.optional[
        list[io_k8s_api_core_v1_PodResourceClaimStatus]
    ]
    startTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]


@core.schema
class io_k8s_api_core_v1_Probe:
    """Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic."""

    """Dependencies: ['io.k8s.api.core.v1.ExecAction', 'io.k8s.api.core.v1.GRPCAction', 'io.k8s.api.core.v1.HTTPGetAction', 'io.k8s.api.core.v1.TCPSocketAction']"""
    exec: core.optional[io_k8s_api_core_v1_ExecAction]
    failureThreshold: core.optional[int]
    grpc: core.optional[io_k8s_api_core_v1_GRPCAction]
    httpGet: core.optional[io_k8s_api_core_v1_HTTPGetAction]
    initialDelaySeconds: core.optional[int]
    periodSeconds: core.optional[int]
    successThreshold: core.optional[int]
    tcpSocket: core.optional[io_k8s_api_core_v1_TCPSocketAction]
    terminationGracePeriodSeconds: core.optional[int]
    timeoutSeconds: core.optional[int]


@core.schema
class io_k8s_api_core_v1_ResourceQuotaSpec:
    """ResourceQuotaSpec defines the desired hard limits to enforce for Quota."""

    """Dependencies: ['io.k8s.api.core.v1.ScopeSelector']"""
    hard: core.optional[dict[str, str]]
    scopeSelector: core.optional[io_k8s_api_core_v1_ScopeSelector]
    scopes: core.optional[list[str]]


@core.schema
class io_k8s_api_core_v1_Secret:
    """Secret holds secret data of a certain type. The total bytes of the values in the Data field must be less than MaxSecretSize bytes."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    apiVersion: core.optional[str]
    data: core.optional[dict[str, str]]
    immutable: core.optional[bool]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    stringData: core.optional[dict[str, str]]
    type: core.optional[str]


@core.schema
class io_k8s_api_core_v1_SecretList:
    """SecretList is a list of Secret."""

    """Dependencies: ['io.k8s.api.core.v1.Secret', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_Secret]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_ServiceAccount:
    """ServiceAccount binds together: * a name, understood by users, and perhaps by peripheral systems, for an identity * a principal that can be authenticated and authorized * a set of secrets"""

    """Dependencies: ['io.k8s.api.core.v1.LocalObjectReference', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.ObjectReference']"""
    apiVersion: core.optional[str]
    automountServiceAccountToken: core.optional[bool]
    imagePullSecrets: core.optional[list[io_k8s_api_core_v1_LocalObjectReference]]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    secrets: core.optional[list[io_k8s_api_core_v1_ObjectReference]]


@core.schema
class io_k8s_api_core_v1_ServiceAccountList:
    """ServiceAccountList is a list of ServiceAccount objects"""

    """Dependencies: ['io.k8s.api.core.v1.ServiceAccount', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_ServiceAccount]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_ServiceStatus:
    """ServiceStatus represents the current status of a service."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Condition', 'io.k8s.api.core.v1.LoadBalancerStatus']"""
    conditions: core.optional[list[io_k8s_apimachinery_pkg_apis_meta_v1_Condition]]
    loadBalancer: core.optional[io_k8s_api_core_v1_LoadBalancerStatus]


@core.schema
class io_k8s_api_core_v1_TopologySpreadConstraint:
    """TopologySpreadConstraint specifies how to spread matching pods among the given topology."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    labelSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    matchLabelKeys: core.optional[list[str]]
    maxSkew: int
    minDomains: core.optional[int]
    nodeAffinityPolicy: core.optional[str]
    nodeTaintsPolicy: core.optional[str]
    topologyKey: str
    whenUnsatisfiable: str


@core.schema
class io_k8s_api_core_v1_WeightedPodAffinityTerm:
    """The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)"""

    """Dependencies: ['io.k8s.api.core.v1.PodAffinityTerm']"""
    podAffinityTerm: io_k8s_api_core_v1_PodAffinityTerm
    weight: int


@core.schema
class io_k8s_api_discovery_v1_Endpoint:
    """Endpoint represents a single logical "backend" implementing a service."""

    """Dependencies: ['io.k8s.api.discovery.v1.EndpointConditions', 'io.k8s.api.discovery.v1.EndpointHints', 'io.k8s.api.core.v1.ObjectReference']"""
    addresses: list[str]
    conditions: core.optional[io_k8s_api_discovery_v1_EndpointConditions]
    deprecatedTopology: core.optional[dict[str, str]]
    hints: core.optional[io_k8s_api_discovery_v1_EndpointHints]
    hostname: core.optional[str]
    nodeName: core.optional[str]
    targetRef: core.optional[io_k8s_api_core_v1_ObjectReference]
    zone: core.optional[str]


@core.schema
class io_k8s_api_discovery_v1_EndpointSlice:
    """EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints."""

    """Dependencies: ['io.k8s.api.discovery.v1.Endpoint', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.discovery.v1.EndpointPort']"""
    addressType: str
    apiVersion: core.optional[str]
    endpoints: list[io_k8s_api_discovery_v1_Endpoint]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    ports: core.optional[list[io_k8s_api_discovery_v1_EndpointPort]]


@core.schema
class io_k8s_api_discovery_v1_EndpointSliceList:
    """EndpointSliceList represents a list of endpoint slices"""

    """Dependencies: ['io.k8s.api.discovery.v1.EndpointSlice', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_discovery_v1_EndpointSlice]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_events_v1_Event:
    """Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time', 'io.k8s.api.core.v1.EventSource', 'io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.ObjectReference', 'io.k8s.api.core.v1.ObjectReference', 'io.k8s.api.events.v1.EventSeries']"""
    action: core.optional[str]
    apiVersion: core.optional[str]
    deprecatedCount: core.optional[int]
    deprecatedFirstTimestamp: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    deprecatedLastTimestamp: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    deprecatedSource: core.optional[io_k8s_api_core_v1_EventSource]
    eventTime: io_k8s_apimachinery_pkg_apis_meta_v1_MicroTime
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    note: core.optional[str]
    reason: core.optional[str]
    regarding: core.optional[io_k8s_api_core_v1_ObjectReference]
    related: core.optional[io_k8s_api_core_v1_ObjectReference]
    reportingController: core.optional[str]
    reportingInstance: core.optional[str]
    series: core.optional[io_k8s_api_events_v1_EventSeries]
    type: core.optional[str]


@core.schema
class io_k8s_api_events_v1_EventList:
    """EventList is a list of Event objects."""

    """Dependencies: ['io.k8s.api.events.v1.Event', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_events_v1_Event]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_flowcontrol_v1_PolicyRulesWithSubjects:
    """PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.NonResourcePolicyRule', 'io.k8s.api.flowcontrol.v1.ResourcePolicyRule', 'io.k8s.api.flowcontrol.v1.Subject']"""
    nonResourceRules: core.optional[
        list[io_k8s_api_flowcontrol_v1_NonResourcePolicyRule]
    ]
    resourceRules: core.optional[list[io_k8s_api_flowcontrol_v1_ResourcePolicyRule]]
    subjects: list[io_k8s_api_flowcontrol_v1_Subject]


@core.schema
class io_k8s_api_flowcontrol_v1_PriorityLevelConfiguration:
    """PriorityLevelConfiguration represents the configuration of a priority level."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationSpec', 'io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationSpec]
    status: core.optional[io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationStatus]


@core.schema
class io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationList:
    """PriorityLevelConfigurationList is a list of PriorityLevelConfiguration objects."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.PriorityLevelConfiguration', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_flowcontrol_v1_PriorityLevelConfiguration]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_PolicyRulesWithSubjects:
    """PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.NonResourcePolicyRule', 'io.k8s.api.flowcontrol.v1beta3.ResourcePolicyRule', 'io.k8s.api.flowcontrol.v1beta3.Subject']"""
    nonResourceRules: core.optional[
        list[io_k8s_api_flowcontrol_v1beta3_NonResourcePolicyRule]
    ]
    resourceRules: core.optional[
        list[io_k8s_api_flowcontrol_v1beta3_ResourcePolicyRule]
    ]
    subjects: list[io_k8s_api_flowcontrol_v1beta3_Subject]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfiguration:
    """PriorityLevelConfiguration represents the configuration of a priority level."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.flowcontrol.v1beta3.PriorityLevelConfigurationSpec', 'io.k8s.api.flowcontrol.v1beta3.PriorityLevelConfigurationStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationSpec]
    status: core.optional[
        io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationStatus
    ]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationList:
    """PriorityLevelConfigurationList is a list of PriorityLevelConfiguration objects."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.PriorityLevelConfiguration', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfiguration]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_networking_v1_IngressBackend:
    """IngressBackend describes all endpoints for a given service and port."""

    """Dependencies: ['io.k8s.api.core.v1.TypedLocalObjectReference', 'io.k8s.api.networking.v1.IngressServiceBackend']"""
    resource: core.optional[io_k8s_api_core_v1_TypedLocalObjectReference]
    service: core.optional[io_k8s_api_networking_v1_IngressServiceBackend]


@core.schema
class io_k8s_api_networking_v1_IngressClass:
    """IngressClass represents the class of the Ingress, referenced by the Ingress Spec. The `ingressclass.kubernetes.io/is-default-class` annotation can be used to indicate that an IngressClass should be considered default. When a single IngressClass resource has this annotation set to true, new Ingress resources without a class specified will be assigned this default class."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.networking.v1.IngressClassSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_networking_v1_IngressClassSpec]


@core.schema
class io_k8s_api_networking_v1_IngressClassList:
    """IngressClassList is a collection of IngressClasses."""

    """Dependencies: ['io.k8s.api.networking.v1.IngressClass', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_networking_v1_IngressClass]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_networking_v1_NetworkPolicyPeer:
    """NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed"""

    """Dependencies: ['io.k8s.api.networking.v1.IPBlock', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    ipBlock: core.optional[io_k8s_api_networking_v1_IPBlock]
    namespaceSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    podSelector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]


@core.schema
class io_k8s_api_networking_v1alpha1_IPAddress:
    """IPAddress represents a single IP of a single IP Family. The object is designed to be used by APIs that operate on IP addresses. The object is used by the Service core API for allocation of IP addresses. An IP address can be represented in different formats, to guarantee the uniqueness of the IP, the name of the object is the IP address in canonical format, four decimal digits separated by dots suppressing leading zeros for IPv4 and the representation defined by RFC 5952 for IPv6. Valid: 192.168.1.5 or 2001:db8::1 or 2001:db8:aaaa:bbbb:cccc:dddd:eeee:1 Invalid: 10.01.2.3 or 2001:db8:0:0:0::1"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.networking.v1alpha1.IPAddressSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_networking_v1alpha1_IPAddressSpec]


@core.schema
class io_k8s_api_networking_v1alpha1_IPAddressList:
    """IPAddressList contains a list of IPAddress."""

    """Dependencies: ['io.k8s.api.networking.v1alpha1.IPAddress', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_networking_v1alpha1_IPAddress]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_networking_v1alpha1_ServiceCIDRStatus:
    """ServiceCIDRStatus describes the current state of the ServiceCIDR."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Condition']"""
    conditions: core.optional[list[io_k8s_apimachinery_pkg_apis_meta_v1_Condition]]


@core.schema
class io_k8s_api_node_v1_RuntimeClass:
    """RuntimeClass defines a class of container runtime supported in the cluster. The RuntimeClass is used to determine which container runtime is used to run all containers in a pod. RuntimeClasses are manually defined by a user or cluster provisioner, and referenced in the PodSpec. The Kubelet is responsible for resolving the RuntimeClassName reference before running the pod.  For more details, see https://kubernetes.io/docs/concepts/containers/runtime-class/"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.node.v1.Overhead', 'io.k8s.api.node.v1.Scheduling']"""
    apiVersion: core.optional[str]
    handler: str
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    overhead: core.optional[io_k8s_api_node_v1_Overhead]
    scheduling: core.optional[io_k8s_api_node_v1_Scheduling]


@core.schema
class io_k8s_api_node_v1_RuntimeClassList:
    """RuntimeClassList is a list of RuntimeClass objects."""

    """Dependencies: ['io.k8s.api.node.v1.RuntimeClass', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_node_v1_RuntimeClass]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_policy_v1_Eviction:
    """Eviction evicts a pod from its node subject to certain policies and safety constraints. This is a subresource of Pod.  A request to cause such an eviction is created by POSTing to .../pods/<pod name>/evictions."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.DeleteOptions', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    apiVersion: core.optional[str]
    deleteOptions: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_DeleteOptions]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]


@core.schema
class io_k8s_api_policy_v1_PodDisruptionBudgetSpec:
    """PodDisruptionBudgetSpec is a description of a PodDisruptionBudget."""

    """Dependencies: ['io.k8s.apimachinery.pkg.util.intstr.IntOrString', 'io.k8s.apimachinery.pkg.util.intstr.IntOrString', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    maxUnavailable: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]
    minAvailable: core.optional[io_k8s_apimachinery_pkg_util_intstr_IntOrString]
    selector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    unhealthyPodEvictionPolicy: core.optional[str]


@core.schema
class io_k8s_api_policy_v1_PodDisruptionBudgetStatus:
    """PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget. Status may trail the actual state of a system."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.Condition']"""
    conditions: core.optional[list[io_k8s_apimachinery_pkg_apis_meta_v1_Condition]]
    currentHealthy: int
    desiredHealthy: int
    disruptedPods: core.optional[dict[str, str]]
    disruptionsAllowed: int
    expectedPods: int
    observedGeneration: core.optional[int]


@core.schema
class io_k8s_api_rbac_v1_AggregationRule:
    """AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    clusterRoleSelectors: core.optional[
        list[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    ]


@core.schema
class io_k8s_api_rbac_v1_ClusterRole:
    """ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding."""

    """Dependencies: ['io.k8s.api.rbac.v1.AggregationRule', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.rbac.v1.PolicyRule']"""
    aggregationRule: core.optional[io_k8s_api_rbac_v1_AggregationRule]
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    rules: core.optional[list[io_k8s_api_rbac_v1_PolicyRule]]


@core.schema
class io_k8s_api_rbac_v1_ClusterRoleBinding:
    """ClusterRoleBinding references a ClusterRole, but not contain it.  It can reference a ClusterRole in the global namespace, and adds who information via Subject."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.rbac.v1.RoleRef', 'io.k8s.api.rbac.v1.Subject']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    roleRef: io_k8s_api_rbac_v1_RoleRef
    subjects: core.optional[list[io_k8s_api_rbac_v1_Subject]]


@core.schema
class io_k8s_api_rbac_v1_ClusterRoleBindingList:
    """ClusterRoleBindingList is a collection of ClusterRoleBindings"""

    """Dependencies: ['io.k8s.api.rbac.v1.ClusterRoleBinding', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_rbac_v1_ClusterRoleBinding]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_rbac_v1_ClusterRoleList:
    """ClusterRoleList is a collection of ClusterRoles"""

    """Dependencies: ['io.k8s.api.rbac.v1.ClusterRole', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_rbac_v1_ClusterRole]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_rbac_v1_Role:
    """Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.rbac.v1.PolicyRule']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    rules: core.optional[list[io_k8s_api_rbac_v1_PolicyRule]]


@core.schema
class io_k8s_api_rbac_v1_RoleBinding:
    """RoleBinding references a role, but does not contain it.  It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in.  RoleBindings in a given namespace only have effect in that namespace."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.rbac.v1.RoleRef', 'io.k8s.api.rbac.v1.Subject']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    roleRef: io_k8s_api_rbac_v1_RoleRef
    subjects: core.optional[list[io_k8s_api_rbac_v1_Subject]]


@core.schema
class io_k8s_api_rbac_v1_RoleBindingList:
    """RoleBindingList is a collection of RoleBindings"""

    """Dependencies: ['io.k8s.api.rbac.v1.RoleBinding', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_rbac_v1_RoleBinding]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_rbac_v1_RoleList:
    """RoleList is a collection of Roles"""

    """Dependencies: ['io.k8s.api.rbac.v1.Role', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_rbac_v1_Role]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_resource_v1alpha2_DriverRequests:
    """DriverRequests describes all resources that are needed from one particular driver."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceRequest', 'io.k8s.apimachinery.pkg.runtime.RawExtension']"""
    driverName: core.optional[str]
    requests: core.optional[list[io_k8s_api_resource_v1alpha2_ResourceRequest]]
    vendorParameters: core.optional[io_k8s_apimachinery_pkg_runtime_RawExtension]


@core.schema
class io_k8s_api_resource_v1alpha2_PodSchedulingContext:
    """PodSchedulingContext objects hold information that is needed to schedule a Pod with ResourceClaims that use "WaitForFirstConsumer" allocation mode.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.resource.v1alpha2.PodSchedulingContextSpec', 'io.k8s.api.resource.v1alpha2.PodSchedulingContextStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_resource_v1alpha2_PodSchedulingContextSpec
    status: core.optional[io_k8s_api_resource_v1alpha2_PodSchedulingContextStatus]


@core.schema
class io_k8s_api_resource_v1alpha2_PodSchedulingContextList:
    """PodSchedulingContextList is a collection of Pod scheduling objects."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.PodSchedulingContext', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_resource_v1alpha2_PodSchedulingContext]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimParameters:
    """ResourceClaimParameters defines resource requests for a ResourceClaim in an in-tree format understood by Kubernetes."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.DriverRequests', 'io.k8s.api.resource.v1alpha2.ResourceClaimParametersReference', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    apiVersion: core.optional[str]
    driverRequests: core.optional[list[io_k8s_api_resource_v1alpha2_DriverRequests]]
    generatedFrom: core.optional[
        io_k8s_api_resource_v1alpha2_ResourceClaimParametersReference
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    shareable: core.optional[bool]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimParametersList:
    """ResourceClaimParametersList is a collection of ResourceClaimParameters."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceClaimParameters', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_resource_v1alpha2_ResourceClaimParameters]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimTemplateSpec:
    """ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.resource.v1alpha2.ResourceClaimSpec']"""
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_resource_v1alpha2_ResourceClaimSpec


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClass:
    """ResourceClass is used by administrators to influence how resources are allocated.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.resource.v1alpha2.ResourceClassParametersReference', 'io.k8s.api.core.v1.NodeSelector']"""
    apiVersion: core.optional[str]
    driverName: str
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    parametersRef: core.optional[
        io_k8s_api_resource_v1alpha2_ResourceClassParametersReference
    ]
    structuredParameters: core.optional[bool]
    suitableNodes: core.optional[io_k8s_api_core_v1_NodeSelector]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClassList:
    """ResourceClassList is a collection of classes."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceClass', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_resource_v1alpha2_ResourceClass]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClassParameters:
    """ResourceClassParameters defines resource requests for a ResourceClass in an in-tree format understood by Kubernetes."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceFilter', 'io.k8s.api.resource.v1alpha2.ResourceClassParametersReference', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.resource.v1alpha2.VendorParameters']"""
    apiVersion: core.optional[str]
    filters: core.optional[list[io_k8s_api_resource_v1alpha2_ResourceFilter]]
    generatedFrom: core.optional[
        io_k8s_api_resource_v1alpha2_ResourceClassParametersReference
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    vendorParameters: core.optional[list[io_k8s_api_resource_v1alpha2_VendorParameters]]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClassParametersList:
    """ResourceClassParametersList is a collection of ResourceClassParameters."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceClassParameters', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_resource_v1alpha2_ResourceClassParameters]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceHandle:
    """ResourceHandle holds opaque resource data for processing by a specific kubelet plugin."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.StructuredResourceHandle']"""
    data: core.optional[str]
    driverName: str
    structuredData: core.optional[io_k8s_api_resource_v1alpha2_StructuredResourceHandle]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceSlice:
    """ResourceSlice provides information about available resources on individual nodes."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.resource.v1alpha2.NamedResourcesResources']"""
    apiVersion: core.optional[str]
    driverName: str
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    namedResources: core.optional[io_k8s_api_resource_v1alpha2_NamedResourcesResources]
    nodeName: core.optional[str]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceSliceList:
    """ResourceSliceList is a collection of ResourceSlices."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceSlice', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_resource_v1alpha2_ResourceSlice]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_scheduling_v1_PriorityClass:
    """PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    apiVersion: core.optional[str]
    description: core.optional[str]
    globalDefault: core.optional[bool]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    preemptionPolicy: core.optional[str]
    value: int


@core.schema
class io_k8s_api_scheduling_v1_PriorityClassList:
    """PriorityClassList is a collection of priority classes."""

    """Dependencies: ['io.k8s.api.scheduling.v1.PriorityClass', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_scheduling_v1_PriorityClass]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_storage_v1_CSIDriver:
    """CSIDriver captures information about a Container Storage Interface (CSI) volume driver deployed on the cluster. Kubernetes attach detach controller uses this object to determine whether attach is required. Kubelet uses this object to determine whether pod information needs to be passed on mount. CSIDriver objects are non-namespaced."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.storage.v1.CSIDriverSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_storage_v1_CSIDriverSpec


@core.schema
class io_k8s_api_storage_v1_CSIDriverList:
    """CSIDriverList is a collection of CSIDriver objects."""

    """Dependencies: ['io.k8s.api.storage.v1.CSIDriver', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_storage_v1_CSIDriver]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_storage_v1_CSINode:
    """CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to create the CSINode object directly. As long as they use the node-driver-registrar sidecar container, the kubelet will automatically populate the CSINode object for the CSI driver as part of kubelet plugin registration. CSINode has the same name as a node. If the object is missing, it means either there are no CSI Drivers available on the node, or the Kubelet version is low enough that it doesn't create this object. CSINode has an OwnerReference that points to the corresponding node object."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.storage.v1.CSINodeSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_storage_v1_CSINodeSpec


@core.schema
class io_k8s_api_storage_v1_CSINodeList:
    """CSINodeList is a collection of CSINode objects."""

    """Dependencies: ['io.k8s.api.storage.v1.CSINode', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_storage_v1_CSINode]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_storage_v1_CSIStorageCapacity:
    """CSIStorageCapacity stores the result of one CSI GetCapacity call. For a given StorageClass, this describes the available capacity in a particular topology segment.  This can be used when considering where to instantiate new PersistentVolumes.

    For example this can express things like: - StorageClass "standard" has "1234 GiB" available in "topology.kubernetes.io/zone=us-east1" - StorageClass "localssd" has "10 GiB" available in "kubernetes.io/hostname=knode-abc123"

    The following three cases all imply that no capacity is available for a certain combination: - no object exists with suitable topology and storage class name - such an object exists, but the capacity is unset - such an object exists, but the capacity is zero

    The producer of these objects can decide which approach is more suitable.

    They are consumed by the kube-scheduler when a CSI driver opts into capacity-aware scheduling with CSIDriverSpec.StorageCapacity. The scheduler compares the MaximumVolumeSize against the requested size of pending volumes to filter out unsuitable nodes. If MaximumVolumeSize is unset, it falls back to a comparison against the less precise Capacity. If that is also unset, the scheduler assumes that capacity is insufficient and tries some other node.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.api.resource.Quantity', 'io.k8s.apimachinery.pkg.api.resource.Quantity', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    apiVersion: core.optional[str]
    capacity: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]
    kind: core.optional[str]
    maximumVolumeSize: core.optional[io_k8s_apimachinery_pkg_api_resource_Quantity]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    nodeTopology: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    storageClassName: str


@core.schema
class io_k8s_api_storage_v1_CSIStorageCapacityList:
    """CSIStorageCapacityList is a collection of CSIStorageCapacity objects."""

    """Dependencies: ['io.k8s.api.storage.v1.CSIStorageCapacity', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_storage_v1_CSIStorageCapacity]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_storage_v1_StorageClass:
    """StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.

    StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name.
    """

    """Dependencies: ['io.k8s.api.core.v1.TopologySelectorTerm', 'io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    allowVolumeExpansion: core.optional[bool]
    allowedTopologies: core.optional[list[io_k8s_api_core_v1_TopologySelectorTerm]]
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    mountOptions: core.optional[list[str]]
    parameters: core.optional[dict[str, str]]
    provisioner: str
    reclaimPolicy: core.optional[str]
    volumeBindingMode: core.optional[str]


@core.schema
class io_k8s_api_storage_v1_StorageClassList:
    """StorageClassList is a collection of storage classes."""

    """Dependencies: ['io.k8s.api.storage.v1.StorageClass', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_storage_v1_StorageClass]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_storage_v1_VolumeAttachmentSource:
    """VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one member can be set."""

    """Dependencies: ['io.k8s.api.core.v1.PersistentVolumeSpec']"""
    inlineVolumeSpec: core.optional[io_k8s_api_core_v1_PersistentVolumeSpec]
    persistentVolumeName: core.optional[str]


@core.schema
class io_k8s_api_storage_v1_VolumeAttachmentSpec:
    """VolumeAttachmentSpec is the specification of a VolumeAttachment request."""

    """Dependencies: ['io.k8s.api.storage.v1.VolumeAttachmentSource']"""
    attacher: str
    nodeName: str
    source: io_k8s_api_storage_v1_VolumeAttachmentSource


@core.schema
class io_k8s_api_storage_v1_VolumeAttachmentStatus:
    """VolumeAttachmentStatus is the status of a VolumeAttachment request."""

    """Dependencies: ['io.k8s.api.storage.v1.VolumeError', 'io.k8s.api.storage.v1.VolumeError']"""
    attachError: core.optional[io_k8s_api_storage_v1_VolumeError]
    attached: bool
    attachmentMetadata: core.optional[dict[str, str]]
    detachError: core.optional[io_k8s_api_storage_v1_VolumeError]


@core.schema
class io_k8s_api_storage_v1alpha1_VolumeAttributesClass:
    """VolumeAttributesClass represents a specification of mutable volume attributes defined by the CSI driver. The class can be specified during dynamic provisioning of PersistentVolumeClaims, and changed in the PersistentVolumeClaim spec after provisioning."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta']"""
    apiVersion: core.optional[str]
    driverName: str
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    parameters: core.optional[dict[str, str]]


@core.schema
class io_k8s_api_storage_v1alpha1_VolumeAttributesClassList:
    """VolumeAttributesClassList is a collection of VolumeAttributesClass objects."""

    """Dependencies: ['io.k8s.api.storage.v1alpha1.VolumeAttributesClass', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_storage_v1alpha1_VolumeAttributesClass]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_storagemigration_v1alpha1_StorageVersionMigration:
    """StorageVersionMigration represents a migration of stored data to the latest storage version."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.storagemigration.v1alpha1.StorageVersionMigrationSpec', 'io.k8s.api.storagemigration.v1alpha1.StorageVersionMigrationStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[
        io_k8s_api_storagemigration_v1alpha1_StorageVersionMigrationSpec
    ]
    status: core.optional[
        io_k8s_api_storagemigration_v1alpha1_StorageVersionMigrationStatus
    ]


@core.schema
class io_k8s_api_storagemigration_v1alpha1_StorageVersionMigrationList:
    """StorageVersionMigrationList is a collection of storage version migrations."""

    """Dependencies: ['io.k8s.api.storagemigration.v1alpha1.StorageVersionMigration', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_storagemigration_v1alpha1_StorageVersionMigration]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionSpec:
    """CustomResourceDefinitionSpec describes how a user wants their resource to appear"""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceConversion', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionNames', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionVersion']"""
    conversion: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceConversion
    ]
    group: str
    names: io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionNames
    preserveUnknownFields: core.optional[bool]
    scope: str
    versions: list[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionVersion
    ]


@core.schema
class io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIService:
    """APIService represents a server for a particular GroupVersion. Name must be "version.group"."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.APIServiceSpec', 'io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.APIServiceStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[
        io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIServiceSpec
    ]
    status: core.optional[
        io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIServiceStatus
    ]


@core.schema
class io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIServiceList:
    """APIServiceList is a list of APIService objects."""

    """Dependencies: ['io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.APIService', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_kube_aggregator_pkg_apis_apiregistration_v1_APIService]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicy:
    """ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicySpec', 'io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[
        io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicySpec
    ]
    status: core.optional[
        io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicyStatus
    ]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicyBinding:
    """ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.

    For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the number of parameters selected by the binding.

    The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyBindingSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[
        io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicyBindingSpec
    ]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicyBindingList:
    """ValidatingAdmissionPolicyBindingList is a list of ValidatingAdmissionPolicyBinding."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyBinding', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: core.optional[
        list[io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicyBinding]
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicyList:
    """ValidatingAdmissionPolicyList is a list of ValidatingAdmissionPolicy."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicy', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: core.optional[
        list[io_k8s_api_admissionregistration_v1_ValidatingAdmissionPolicy]
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicy:
    """ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicySpec', 'io.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicyStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[
        io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicySpec
    ]
    status: core.optional[
        io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicyStatus
    ]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicyBinding:
    """ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.

    For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the number of parameters selected by the binding.

    The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicyBindingSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[
        io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicyBindingSpec
    ]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicyBindingList:
    """ValidatingAdmissionPolicyBindingList is a list of ValidatingAdmissionPolicyBinding."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicyBinding', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: core.optional[
        list[io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicyBinding]
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicyList:
    """ValidatingAdmissionPolicyList is a list of ValidatingAdmissionPolicy."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1alpha1.ValidatingAdmissionPolicy', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: core.optional[
        list[io_k8s_api_admissionregistration_v1alpha1_ValidatingAdmissionPolicy]
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicy:
    """ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.admissionregistration.v1beta1.ValidatingAdmissionPolicySpec', 'io.k8s.api.admissionregistration.v1beta1.ValidatingAdmissionPolicyStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[
        io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicySpec
    ]
    status: core.optional[
        io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicyStatus
    ]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicyBinding:
    """ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.

    For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the number of parameters selected by the binding.

    The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.admissionregistration.v1beta1.ValidatingAdmissionPolicyBindingSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[
        io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicyBindingSpec
    ]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicyBindingList:
    """ValidatingAdmissionPolicyBindingList is a list of ValidatingAdmissionPolicyBinding."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1beta1.ValidatingAdmissionPolicyBinding', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: core.optional[
        list[io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicyBinding]
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicyList:
    """ValidatingAdmissionPolicyList is a list of ValidatingAdmissionPolicy."""

    """Dependencies: ['io.k8s.api.admissionregistration.v1beta1.ValidatingAdmissionPolicy', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: core.optional[
        list[io_k8s_api_admissionregistration_v1beta1_ValidatingAdmissionPolicy]
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_autoscaling_v2_ExternalMetricSource:
    """ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricIdentifier', 'io.k8s.api.autoscaling.v2.MetricTarget']"""
    metric: io_k8s_api_autoscaling_v2_MetricIdentifier
    target: io_k8s_api_autoscaling_v2_MetricTarget


@core.schema
class io_k8s_api_autoscaling_v2_ExternalMetricStatus:
    """ExternalMetricStatus indicates the current value of a global metric not associated with any Kubernetes object."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.MetricValueStatus', 'io.k8s.api.autoscaling.v2.MetricIdentifier']"""
    current: io_k8s_api_autoscaling_v2_MetricValueStatus
    metric: io_k8s_api_autoscaling_v2_MetricIdentifier


@core.schema
class io_k8s_api_autoscaling_v2_MetricSpec:
    """MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once)."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.ContainerResourceMetricSource', 'io.k8s.api.autoscaling.v2.ExternalMetricSource', 'io.k8s.api.autoscaling.v2.ObjectMetricSource', 'io.k8s.api.autoscaling.v2.PodsMetricSource', 'io.k8s.api.autoscaling.v2.ResourceMetricSource']"""
    containerResource: core.optional[
        io_k8s_api_autoscaling_v2_ContainerResourceMetricSource
    ]
    external: core.optional[io_k8s_api_autoscaling_v2_ExternalMetricSource]
    object: core.optional[io_k8s_api_autoscaling_v2_ObjectMetricSource]
    pods: core.optional[io_k8s_api_autoscaling_v2_PodsMetricSource]
    resource: core.optional[io_k8s_api_autoscaling_v2_ResourceMetricSource]
    type: str


@core.schema
class io_k8s_api_autoscaling_v2_MetricStatus:
    """MetricStatus describes the last-read state of a single metric."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.ContainerResourceMetricStatus', 'io.k8s.api.autoscaling.v2.ExternalMetricStatus', 'io.k8s.api.autoscaling.v2.ObjectMetricStatus', 'io.k8s.api.autoscaling.v2.PodsMetricStatus', 'io.k8s.api.autoscaling.v2.ResourceMetricStatus']"""
    containerResource: core.optional[
        io_k8s_api_autoscaling_v2_ContainerResourceMetricStatus
    ]
    external: core.optional[io_k8s_api_autoscaling_v2_ExternalMetricStatus]
    object: core.optional[io_k8s_api_autoscaling_v2_ObjectMetricStatus]
    pods: core.optional[io_k8s_api_autoscaling_v2_PodsMetricStatus]
    resource: core.optional[io_k8s_api_autoscaling_v2_ResourceMetricStatus]
    type: str


@core.schema
class io_k8s_api_core_v1_DownwardAPIProjection:
    """Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode."""

    """Dependencies: ['io.k8s.api.core.v1.DownwardAPIVolumeFile']"""
    items: core.optional[list[io_k8s_api_core_v1_DownwardAPIVolumeFile]]


@core.schema
class io_k8s_api_core_v1_EnvVar:
    """EnvVar represents an environment variable present in a Container."""

    """Dependencies: ['io.k8s.api.core.v1.EnvVarSource']"""
    name: str
    value: core.optional[str]
    valueFrom: core.optional[io_k8s_api_core_v1_EnvVarSource]


@core.schema
class io_k8s_api_core_v1_EphemeralVolumeSource:
    """Represents an ephemeral volume that is handled by a normal storage driver."""

    """Dependencies: ['io.k8s.api.core.v1.PersistentVolumeClaimTemplate']"""
    volumeClaimTemplate: core.optional[io_k8s_api_core_v1_PersistentVolumeClaimTemplate]


@core.schema
class io_k8s_api_core_v1_Lifecycle:
    """Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted."""

    """Dependencies: ['io.k8s.api.core.v1.LifecycleHandler', 'io.k8s.api.core.v1.LifecycleHandler']"""
    postStart: core.optional[io_k8s_api_core_v1_LifecycleHandler]
    preStop: core.optional[io_k8s_api_core_v1_LifecycleHandler]


@core.schema
class io_k8s_api_core_v1_Node:
    """Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache (i.e. in etcd)."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.NodeSpec', 'io.k8s.api.core.v1.NodeStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_NodeSpec]
    status: core.optional[io_k8s_api_core_v1_NodeStatus]


@core.schema
class io_k8s_api_core_v1_NodeList:
    """NodeList is the whole list of all Nodes which have been registered with master."""

    """Dependencies: ['io.k8s.api.core.v1.Node', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_Node]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_PersistentVolume:
    """PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.PersistentVolumeSpec', 'io.k8s.api.core.v1.PersistentVolumeStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_PersistentVolumeSpec]
    status: core.optional[io_k8s_api_core_v1_PersistentVolumeStatus]


@core.schema
class io_k8s_api_core_v1_PersistentVolumeClaim:
    """PersistentVolumeClaim is a user's request for and claim to a persistent volume"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.PersistentVolumeClaimSpec', 'io.k8s.api.core.v1.PersistentVolumeClaimStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_PersistentVolumeClaimSpec]
    status: core.optional[io_k8s_api_core_v1_PersistentVolumeClaimStatus]


@core.schema
class io_k8s_api_core_v1_PersistentVolumeClaimList:
    """PersistentVolumeClaimList is a list of PersistentVolumeClaim items."""

    """Dependencies: ['io.k8s.api.core.v1.PersistentVolumeClaim', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_PersistentVolumeClaim]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_PersistentVolumeList:
    """PersistentVolumeList is a list of PersistentVolume items."""

    """Dependencies: ['io.k8s.api.core.v1.PersistentVolume', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_PersistentVolume]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_PodAffinity:
    """Pod affinity is a group of inter pod affinity scheduling rules."""

    """Dependencies: ['io.k8s.api.core.v1.WeightedPodAffinityTerm', 'io.k8s.api.core.v1.PodAffinityTerm']"""
    preferredDuringSchedulingIgnoredDuringExecution: core.optional[
        list[io_k8s_api_core_v1_WeightedPodAffinityTerm]
    ]
    requiredDuringSchedulingIgnoredDuringExecution: core.optional[
        list[io_k8s_api_core_v1_PodAffinityTerm]
    ]


@core.schema
class io_k8s_api_core_v1_PodAntiAffinity:
    """Pod anti affinity is a group of inter pod anti affinity scheduling rules."""

    """Dependencies: ['io.k8s.api.core.v1.WeightedPodAffinityTerm', 'io.k8s.api.core.v1.PodAffinityTerm']"""
    preferredDuringSchedulingIgnoredDuringExecution: core.optional[
        list[io_k8s_api_core_v1_WeightedPodAffinityTerm]
    ]
    requiredDuringSchedulingIgnoredDuringExecution: core.optional[
        list[io_k8s_api_core_v1_PodAffinityTerm]
    ]


@core.schema
class io_k8s_api_core_v1_ResourceQuota:
    """ResourceQuota sets aggregate quota restrictions enforced per namespace"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.ResourceQuotaSpec', 'io.k8s.api.core.v1.ResourceQuotaStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_ResourceQuotaSpec]
    status: core.optional[io_k8s_api_core_v1_ResourceQuotaStatus]


@core.schema
class io_k8s_api_core_v1_ResourceQuotaList:
    """ResourceQuotaList is a list of ResourceQuota items."""

    """Dependencies: ['io.k8s.api.core.v1.ResourceQuota', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_ResourceQuota]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_Service:
    """Service is a named abstraction of software service (for example, mysql) consisting of local port (for example 3306) that the proxy listens on, and the selector that determines which pods will answer requests sent through the proxy."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.ServiceSpec', 'io.k8s.api.core.v1.ServiceStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_ServiceSpec]
    status: core.optional[io_k8s_api_core_v1_ServiceStatus]


@core.schema
class io_k8s_api_core_v1_ServiceList:
    """ServiceList holds a list of services."""

    """Dependencies: ['io.k8s.api.core.v1.Service', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_Service]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_VolumeProjection:
    """Projection that may be projected along with other supported volume types"""

    """Dependencies: ['io.k8s.api.core.v1.ClusterTrustBundleProjection', 'io.k8s.api.core.v1.ConfigMapProjection', 'io.k8s.api.core.v1.DownwardAPIProjection', 'io.k8s.api.core.v1.SecretProjection', 'io.k8s.api.core.v1.ServiceAccountTokenProjection']"""
    clusterTrustBundle: core.optional[io_k8s_api_core_v1_ClusterTrustBundleProjection]
    configMap: core.optional[io_k8s_api_core_v1_ConfigMapProjection]
    downwardAPI: core.optional[io_k8s_api_core_v1_DownwardAPIProjection]
    secret: core.optional[io_k8s_api_core_v1_SecretProjection]
    serviceAccountToken: core.optional[io_k8s_api_core_v1_ServiceAccountTokenProjection]


@core.schema
class io_k8s_api_flowcontrol_v1_FlowSchemaSpec:
    """FlowSchemaSpec describes how the FlowSchema's specification looks like."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.FlowDistinguisherMethod', 'io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationReference', 'io.k8s.api.flowcontrol.v1.PolicyRulesWithSubjects']"""
    distinguisherMethod: core.optional[
        io_k8s_api_flowcontrol_v1_FlowDistinguisherMethod
    ]
    matchingPrecedence: core.optional[int]
    priorityLevelConfiguration: (
        io_k8s_api_flowcontrol_v1_PriorityLevelConfigurationReference
    )
    rules: core.optional[list[io_k8s_api_flowcontrol_v1_PolicyRulesWithSubjects]]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_FlowSchemaSpec:
    """FlowSchemaSpec describes how the FlowSchema's specification looks like."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.FlowDistinguisherMethod', 'io.k8s.api.flowcontrol.v1beta3.PriorityLevelConfigurationReference', 'io.k8s.api.flowcontrol.v1beta3.PolicyRulesWithSubjects']"""
    distinguisherMethod: core.optional[
        io_k8s_api_flowcontrol_v1beta3_FlowDistinguisherMethod
    ]
    matchingPrecedence: core.optional[int]
    priorityLevelConfiguration: (
        io_k8s_api_flowcontrol_v1beta3_PriorityLevelConfigurationReference
    )
    rules: core.optional[list[io_k8s_api_flowcontrol_v1beta3_PolicyRulesWithSubjects]]


@core.schema
class io_k8s_api_networking_v1_HTTPIngressPath:
    """HTTPIngressPath associates a path with a backend. Incoming urls matching the path are forwarded to the backend."""

    """Dependencies: ['io.k8s.api.networking.v1.IngressBackend']"""
    backend: io_k8s_api_networking_v1_IngressBackend
    path: core.optional[str]
    pathType: str


@core.schema
class io_k8s_api_networking_v1_HTTPIngressRuleValue:
    """HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'."""

    """Dependencies: ['io.k8s.api.networking.v1.HTTPIngressPath']"""
    paths: list[io_k8s_api_networking_v1_HTTPIngressPath]


@core.schema
class io_k8s_api_networking_v1_IngressRule:
    """IngressRule represents the rules mapping the paths under a specified host to the related backend services. Incoming requests are first evaluated for a host match, then routed to the backend associated with the matching IngressRuleValue."""

    """Dependencies: ['io.k8s.api.networking.v1.HTTPIngressRuleValue']"""
    host: core.optional[str]
    http: core.optional[io_k8s_api_networking_v1_HTTPIngressRuleValue]


@core.schema
class io_k8s_api_networking_v1_IngressSpec:
    """IngressSpec describes the Ingress the user wishes to exist."""

    """Dependencies: ['io.k8s.api.networking.v1.IngressBackend', 'io.k8s.api.networking.v1.IngressRule', 'io.k8s.api.networking.v1.IngressTLS']"""
    defaultBackend: core.optional[io_k8s_api_networking_v1_IngressBackend]
    ingressClassName: core.optional[str]
    rules: core.optional[list[io_k8s_api_networking_v1_IngressRule]]
    tls: core.optional[list[io_k8s_api_networking_v1_IngressTLS]]


@core.schema
class io_k8s_api_networking_v1_NetworkPolicyEgressRule:
    """NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and to. This type is beta-level in 1.8"""

    """Dependencies: ['io.k8s.api.networking.v1.NetworkPolicyPort', 'io.k8s.api.networking.v1.NetworkPolicyPeer']"""
    ports: core.optional[list[io_k8s_api_networking_v1_NetworkPolicyPort]]
    to: core.optional[list[io_k8s_api_networking_v1_NetworkPolicyPeer]]


@core.schema
class io_k8s_api_networking_v1_NetworkPolicyIngressRule:
    """NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and from."""

    """Dependencies: ['io.k8s.api.networking.v1.NetworkPolicyPeer', 'io.k8s.api.networking.v1.NetworkPolicyPort']"""
    from_: core.optional[list[io_k8s_api_networking_v1_NetworkPolicyPeer]]
    ports: core.optional[list[io_k8s_api_networking_v1_NetworkPolicyPort]]


@core.schema
class io_k8s_api_networking_v1_NetworkPolicySpec:
    """NetworkPolicySpec provides the specification of a NetworkPolicy"""

    """Dependencies: ['io.k8s.api.networking.v1.NetworkPolicyEgressRule', 'io.k8s.api.networking.v1.NetworkPolicyIngressRule', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector']"""
    egress: core.optional[list[io_k8s_api_networking_v1_NetworkPolicyEgressRule]]
    ingress: core.optional[list[io_k8s_api_networking_v1_NetworkPolicyIngressRule]]
    podSelector: io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector
    policyTypes: core.optional[list[str]]


@core.schema
class io_k8s_api_networking_v1alpha1_ServiceCIDR:
    """ServiceCIDR defines a range of IP addresses using CIDR format (e.g. 192.168.0.0/24 or 2001:db2::/64). This range is used to allocate ClusterIPs to Service objects."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.networking.v1alpha1.ServiceCIDRSpec', 'io.k8s.api.networking.v1alpha1.ServiceCIDRStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_networking_v1alpha1_ServiceCIDRSpec]
    status: core.optional[io_k8s_api_networking_v1alpha1_ServiceCIDRStatus]


@core.schema
class io_k8s_api_networking_v1alpha1_ServiceCIDRList:
    """ServiceCIDRList contains a list of ServiceCIDR objects."""

    """Dependencies: ['io.k8s.api.networking.v1alpha1.ServiceCIDR', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_networking_v1alpha1_ServiceCIDR]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_policy_v1_PodDisruptionBudget:
    """PodDisruptionBudget is an object to define the max disruption that can be caused to a collection of pods"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.policy.v1.PodDisruptionBudgetSpec', 'io.k8s.api.policy.v1.PodDisruptionBudgetStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_policy_v1_PodDisruptionBudgetSpec]
    status: core.optional[io_k8s_api_policy_v1_PodDisruptionBudgetStatus]


@core.schema
class io_k8s_api_policy_v1_PodDisruptionBudgetList:
    """PodDisruptionBudgetList is a collection of PodDisruptionBudgets."""

    """Dependencies: ['io.k8s.api.policy.v1.PodDisruptionBudget', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_policy_v1_PodDisruptionBudget]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_resource_v1alpha2_AllocationResult:
    """AllocationResult contains attributes of an allocated resource."""

    """Dependencies: ['io.k8s.api.core.v1.NodeSelector', 'io.k8s.api.resource.v1alpha2.ResourceHandle']"""
    availableOnNodes: core.optional[io_k8s_api_core_v1_NodeSelector]
    resourceHandles: core.optional[list[io_k8s_api_resource_v1alpha2_ResourceHandle]]
    shareable: core.optional[bool]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimStatus:
    """ResourceClaimStatus tracks whether the resource has been allocated and what the resulting attributes are."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.AllocationResult', 'io.k8s.api.resource.v1alpha2.ResourceClaimConsumerReference']"""
    allocation: core.optional[io_k8s_api_resource_v1alpha2_AllocationResult]
    deallocationRequested: core.optional[bool]
    driverName: core.optional[str]
    reservedFor: core.optional[
        list[io_k8s_api_resource_v1alpha2_ResourceClaimConsumerReference]
    ]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimTemplate:
    """ResourceClaimTemplate is used to produce ResourceClaim objects."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.resource.v1alpha2.ResourceClaimTemplateSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_resource_v1alpha2_ResourceClaimTemplateSpec


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimTemplateList:
    """ResourceClaimTemplateList is a collection of claim templates."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceClaimTemplate', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_resource_v1alpha2_ResourceClaimTemplate]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_storage_v1_VolumeAttachment:
    """VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

    VolumeAttachment objects are non-namespaced."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.storage.v1.VolumeAttachmentSpec', 'io.k8s.api.storage.v1.VolumeAttachmentStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_storage_v1_VolumeAttachmentSpec
    status: core.optional[io_k8s_api_storage_v1_VolumeAttachmentStatus]


@core.schema
class io_k8s_api_storage_v1_VolumeAttachmentList:
    """VolumeAttachmentList is a collection of VolumeAttachment objects."""

    """Dependencies: ['io.k8s.api.storage.v1.VolumeAttachment', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_storage_v1_VolumeAttachment]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinition:
    """CustomResourceDefinition represents a resource that should be exposed on the API server.  Its name MUST be in the format <.spec.name>.<.spec.group>."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionSpec', 'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionSpec
    status: core.optional[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionStatus
    ]


@core.schema
class io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinitionList:
    """CustomResourceDefinitionList is a list of CustomResourceDefinition objects."""

    """Dependencies: ['io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinition', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[
        io_k8s_apiextensions_apiserver_pkg_apis_apiextensions_v1_CustomResourceDefinition
    ]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerSpec:
    """HorizontalPodAutoscalerSpec describes the desired functionality of the HorizontalPodAutoscaler."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerBehavior', 'io.k8s.api.autoscaling.v2.MetricSpec', 'io.k8s.api.autoscaling.v2.CrossVersionObjectReference']"""
    behavior: core.optional[io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerBehavior]
    maxReplicas: int
    metrics: core.optional[list[io_k8s_api_autoscaling_v2_MetricSpec]]
    minReplicas: core.optional[int]
    scaleTargetRef: io_k8s_api_autoscaling_v2_CrossVersionObjectReference


@core.schema
class io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerStatus:
    """HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerCondition', 'io.k8s.api.autoscaling.v2.MetricStatus', 'io.k8s.apimachinery.pkg.apis.meta.v1.Time']"""
    conditions: core.optional[
        list[io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerCondition]
    ]
    currentMetrics: core.optional[list[io_k8s_api_autoscaling_v2_MetricStatus]]
    currentReplicas: core.optional[int]
    desiredReplicas: int
    lastScaleTime: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_Time]
    observedGeneration: core.optional[int]


@core.schema
class io_k8s_api_core_v1_Affinity:
    """Affinity is a group of affinity scheduling rules."""

    """Dependencies: ['io.k8s.api.core.v1.NodeAffinity', 'io.k8s.api.core.v1.PodAffinity', 'io.k8s.api.core.v1.PodAntiAffinity']"""
    nodeAffinity: core.optional[io_k8s_api_core_v1_NodeAffinity]
    podAffinity: core.optional[io_k8s_api_core_v1_PodAffinity]
    podAntiAffinity: core.optional[io_k8s_api_core_v1_PodAntiAffinity]


@core.schema
class io_k8s_api_core_v1_Container:
    """A single application container that you want to run within a pod."""

    """Dependencies: ['io.k8s.api.core.v1.EnvVar', 'io.k8s.api.core.v1.EnvFromSource', 'io.k8s.api.core.v1.Lifecycle', 'io.k8s.api.core.v1.Probe', 'io.k8s.api.core.v1.ContainerPort', 'io.k8s.api.core.v1.Probe', 'io.k8s.api.core.v1.ContainerResizePolicy', 'io.k8s.api.core.v1.ResourceRequirements', 'io.k8s.api.core.v1.SecurityContext', 'io.k8s.api.core.v1.Probe', 'io.k8s.api.core.v1.VolumeDevice', 'io.k8s.api.core.v1.VolumeMount']"""
    args: core.optional[list[str]]
    command: core.optional[list[str]]
    env: core.optional[list[io_k8s_api_core_v1_EnvVar]]
    envFrom: core.optional[list[io_k8s_api_core_v1_EnvFromSource]]
    image: core.optional[str]
    imagePullPolicy: core.optional[str]
    lifecycle: core.optional[io_k8s_api_core_v1_Lifecycle]
    livenessProbe: core.optional[io_k8s_api_core_v1_Probe]
    name: str
    ports: core.optional[list[io_k8s_api_core_v1_ContainerPort]]
    readinessProbe: core.optional[io_k8s_api_core_v1_Probe]
    resizePolicy: core.optional[list[io_k8s_api_core_v1_ContainerResizePolicy]]
    resources: core.optional[io_k8s_api_core_v1_ResourceRequirements]
    restartPolicy: core.optional[str]
    securityContext: core.optional[io_k8s_api_core_v1_SecurityContext]
    startupProbe: core.optional[io_k8s_api_core_v1_Probe]
    stdin: core.optional[bool]
    stdinOnce: core.optional[bool]
    terminationMessagePath: core.optional[str]
    terminationMessagePolicy: core.optional[str]
    tty: core.optional[bool]
    volumeDevices: core.optional[list[io_k8s_api_core_v1_VolumeDevice]]
    volumeMounts: core.optional[list[io_k8s_api_core_v1_VolumeMount]]
    workingDir: core.optional[str]


@core.schema
class io_k8s_api_core_v1_EphemeralContainer:
    """An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.

    To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.
    """

    """Dependencies: ['io.k8s.api.core.v1.EnvVar', 'io.k8s.api.core.v1.EnvFromSource', 'io.k8s.api.core.v1.Lifecycle', 'io.k8s.api.core.v1.Probe', 'io.k8s.api.core.v1.ContainerPort', 'io.k8s.api.core.v1.Probe', 'io.k8s.api.core.v1.ContainerResizePolicy', 'io.k8s.api.core.v1.ResourceRequirements', 'io.k8s.api.core.v1.SecurityContext', 'io.k8s.api.core.v1.Probe', 'io.k8s.api.core.v1.VolumeDevice', 'io.k8s.api.core.v1.VolumeMount']"""
    args: core.optional[list[str]]
    command: core.optional[list[str]]
    env: core.optional[list[io_k8s_api_core_v1_EnvVar]]
    envFrom: core.optional[list[io_k8s_api_core_v1_EnvFromSource]]
    image: core.optional[str]
    imagePullPolicy: core.optional[str]
    lifecycle: core.optional[io_k8s_api_core_v1_Lifecycle]
    livenessProbe: core.optional[io_k8s_api_core_v1_Probe]
    name: str
    ports: core.optional[list[io_k8s_api_core_v1_ContainerPort]]
    readinessProbe: core.optional[io_k8s_api_core_v1_Probe]
    resizePolicy: core.optional[list[io_k8s_api_core_v1_ContainerResizePolicy]]
    resources: core.optional[io_k8s_api_core_v1_ResourceRequirements]
    restartPolicy: core.optional[str]
    securityContext: core.optional[io_k8s_api_core_v1_SecurityContext]
    startupProbe: core.optional[io_k8s_api_core_v1_Probe]
    stdin: core.optional[bool]
    stdinOnce: core.optional[bool]
    targetContainerName: core.optional[str]
    terminationMessagePath: core.optional[str]
    terminationMessagePolicy: core.optional[str]
    tty: core.optional[bool]
    volumeDevices: core.optional[list[io_k8s_api_core_v1_VolumeDevice]]
    volumeMounts: core.optional[list[io_k8s_api_core_v1_VolumeMount]]
    workingDir: core.optional[str]


@core.schema
class io_k8s_api_core_v1_ProjectedVolumeSource:
    """Represents a projected volume source"""

    """Dependencies: ['io.k8s.api.core.v1.VolumeProjection']"""
    defaultMode: core.optional[int]
    sources: core.optional[list[io_k8s_api_core_v1_VolumeProjection]]


@core.schema
class io_k8s_api_core_v1_Volume:
    """Volume represents a named volume in a pod that may be accessed by any container in the pod."""

    """Dependencies: ['io.k8s.api.core.v1.AWSElasticBlockStoreVolumeSource', 'io.k8s.api.core.v1.AzureDiskVolumeSource', 'io.k8s.api.core.v1.AzureFileVolumeSource', 'io.k8s.api.core.v1.CephFSVolumeSource', 'io.k8s.api.core.v1.CinderVolumeSource', 'io.k8s.api.core.v1.ConfigMapVolumeSource', 'io.k8s.api.core.v1.CSIVolumeSource', 'io.k8s.api.core.v1.DownwardAPIVolumeSource', 'io.k8s.api.core.v1.EmptyDirVolumeSource', 'io.k8s.api.core.v1.EphemeralVolumeSource', 'io.k8s.api.core.v1.FCVolumeSource', 'io.k8s.api.core.v1.FlexVolumeSource', 'io.k8s.api.core.v1.FlockerVolumeSource', 'io.k8s.api.core.v1.GCEPersistentDiskVolumeSource', 'io.k8s.api.core.v1.GitRepoVolumeSource', 'io.k8s.api.core.v1.GlusterfsVolumeSource', 'io.k8s.api.core.v1.HostPathVolumeSource', 'io.k8s.api.core.v1.ISCSIVolumeSource', 'io.k8s.api.core.v1.NFSVolumeSource', 'io.k8s.api.core.v1.PersistentVolumeClaimVolumeSource', 'io.k8s.api.core.v1.PhotonPersistentDiskVolumeSource', 'io.k8s.api.core.v1.PortworxVolumeSource', 'io.k8s.api.core.v1.ProjectedVolumeSource', 'io.k8s.api.core.v1.QuobyteVolumeSource', 'io.k8s.api.core.v1.RBDVolumeSource', 'io.k8s.api.core.v1.ScaleIOVolumeSource', 'io.k8s.api.core.v1.SecretVolumeSource', 'io.k8s.api.core.v1.StorageOSVolumeSource', 'io.k8s.api.core.v1.VsphereVirtualDiskVolumeSource']"""
    awsElasticBlockStore: core.optional[
        io_k8s_api_core_v1_AWSElasticBlockStoreVolumeSource
    ]
    azureDisk: core.optional[io_k8s_api_core_v1_AzureDiskVolumeSource]
    azureFile: core.optional[io_k8s_api_core_v1_AzureFileVolumeSource]
    cephfs: core.optional[io_k8s_api_core_v1_CephFSVolumeSource]
    cinder: core.optional[io_k8s_api_core_v1_CinderVolumeSource]
    configMap: core.optional[io_k8s_api_core_v1_ConfigMapVolumeSource]
    csi: core.optional[io_k8s_api_core_v1_CSIVolumeSource]
    downwardAPI: core.optional[io_k8s_api_core_v1_DownwardAPIVolumeSource]
    emptyDir: core.optional[io_k8s_api_core_v1_EmptyDirVolumeSource]
    ephemeral: core.optional[io_k8s_api_core_v1_EphemeralVolumeSource]
    fc: core.optional[io_k8s_api_core_v1_FCVolumeSource]
    flexVolume: core.optional[io_k8s_api_core_v1_FlexVolumeSource]
    flocker: core.optional[io_k8s_api_core_v1_FlockerVolumeSource]
    gcePersistentDisk: core.optional[io_k8s_api_core_v1_GCEPersistentDiskVolumeSource]
    gitRepo: core.optional[io_k8s_api_core_v1_GitRepoVolumeSource]
    glusterfs: core.optional[io_k8s_api_core_v1_GlusterfsVolumeSource]
    hostPath: core.optional[io_k8s_api_core_v1_HostPathVolumeSource]
    iscsi: core.optional[io_k8s_api_core_v1_ISCSIVolumeSource]
    name: str
    nfs: core.optional[io_k8s_api_core_v1_NFSVolumeSource]
    persistentVolumeClaim: core.optional[
        io_k8s_api_core_v1_PersistentVolumeClaimVolumeSource
    ]
    photonPersistentDisk: core.optional[
        io_k8s_api_core_v1_PhotonPersistentDiskVolumeSource
    ]
    portworxVolume: core.optional[io_k8s_api_core_v1_PortworxVolumeSource]
    projected: core.optional[io_k8s_api_core_v1_ProjectedVolumeSource]
    quobyte: core.optional[io_k8s_api_core_v1_QuobyteVolumeSource]
    rbd: core.optional[io_k8s_api_core_v1_RBDVolumeSource]
    scaleIO: core.optional[io_k8s_api_core_v1_ScaleIOVolumeSource]
    secret: core.optional[io_k8s_api_core_v1_SecretVolumeSource]
    storageos: core.optional[io_k8s_api_core_v1_StorageOSVolumeSource]
    vsphereVolume: core.optional[io_k8s_api_core_v1_VsphereVirtualDiskVolumeSource]


@core.schema
class io_k8s_api_flowcontrol_v1_FlowSchema:
    """FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema and a "flow distinguisher"."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.flowcontrol.v1.FlowSchemaSpec', 'io.k8s.api.flowcontrol.v1.FlowSchemaStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_flowcontrol_v1_FlowSchemaSpec]
    status: core.optional[io_k8s_api_flowcontrol_v1_FlowSchemaStatus]


@core.schema
class io_k8s_api_flowcontrol_v1_FlowSchemaList:
    """FlowSchemaList is a list of FlowSchema objects."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1.FlowSchema', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_flowcontrol_v1_FlowSchema]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_FlowSchema:
    """FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema and a "flow distinguisher"."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.flowcontrol.v1beta3.FlowSchemaSpec', 'io.k8s.api.flowcontrol.v1beta3.FlowSchemaStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_flowcontrol_v1beta3_FlowSchemaSpec]
    status: core.optional[io_k8s_api_flowcontrol_v1beta3_FlowSchemaStatus]


@core.schema
class io_k8s_api_flowcontrol_v1beta3_FlowSchemaList:
    """FlowSchemaList is a list of FlowSchema objects."""

    """Dependencies: ['io.k8s.api.flowcontrol.v1beta3.FlowSchema', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_flowcontrol_v1beta3_FlowSchema]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_networking_v1_Ingress:
    """Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.networking.v1.IngressSpec', 'io.k8s.api.networking.v1.IngressStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_networking_v1_IngressSpec]
    status: core.optional[io_k8s_api_networking_v1_IngressStatus]


@core.schema
class io_k8s_api_networking_v1_IngressList:
    """IngressList is a collection of Ingress."""

    """Dependencies: ['io.k8s.api.networking.v1.Ingress', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_networking_v1_Ingress]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_networking_v1_NetworkPolicy:
    """NetworkPolicy describes what network traffic is allowed for a set of Pods"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.networking.v1.NetworkPolicySpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_networking_v1_NetworkPolicySpec]


@core.schema
class io_k8s_api_networking_v1_NetworkPolicyList:
    """NetworkPolicyList is a list of NetworkPolicy objects."""

    """Dependencies: ['io.k8s.api.networking.v1.NetworkPolicy', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_networking_v1_NetworkPolicy]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaim:
    """ResourceClaim describes which resources are needed by a resource consumer. Its status tracks whether the resource has been allocated and what the resulting attributes are.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.resource.v1alpha2.ResourceClaimSpec', 'io.k8s.api.resource.v1alpha2.ResourceClaimStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: io_k8s_api_resource_v1alpha2_ResourceClaimSpec
    status: core.optional[io_k8s_api_resource_v1alpha2_ResourceClaimStatus]


@core.schema
class io_k8s_api_resource_v1alpha2_ResourceClaimList:
    """ResourceClaimList is a collection of claims."""

    """Dependencies: ['io.k8s.api.resource.v1alpha2.ResourceClaim', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_resource_v1alpha2_ResourceClaim]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_autoscaling_v2_HorizontalPodAutoscaler:
    """HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which automatically manages the replica count of any resource implementing the scale subresource based on the metrics specified."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerSpec', 'io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerSpec]
    status: core.optional[io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerStatus]


@core.schema
class io_k8s_api_autoscaling_v2_HorizontalPodAutoscalerList:
    """HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects."""

    """Dependencies: ['io.k8s.api.autoscaling.v2.HorizontalPodAutoscaler', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_autoscaling_v2_HorizontalPodAutoscaler]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_PodSpec:
    """PodSpec is a description of a pod."""

    """Dependencies: ['io.k8s.api.core.v1.Affinity', 'io.k8s.api.core.v1.Container', 'io.k8s.api.core.v1.PodDNSConfig', 'io.k8s.api.core.v1.EphemeralContainer', 'io.k8s.api.core.v1.HostAlias', 'io.k8s.api.core.v1.LocalObjectReference', 'io.k8s.api.core.v1.Container', 'io.k8s.api.core.v1.PodOS', 'io.k8s.api.core.v1.PodReadinessGate', 'io.k8s.api.core.v1.PodResourceClaim', 'io.k8s.api.core.v1.PodSchedulingGate', 'io.k8s.api.core.v1.PodSecurityContext', 'io.k8s.api.core.v1.Toleration', 'io.k8s.api.core.v1.TopologySpreadConstraint', 'io.k8s.api.core.v1.Volume']"""
    activeDeadlineSeconds: core.optional[int]
    affinity: core.optional[io_k8s_api_core_v1_Affinity]
    automountServiceAccountToken: core.optional[bool]
    containers: list[io_k8s_api_core_v1_Container]
    dnsConfig: core.optional[io_k8s_api_core_v1_PodDNSConfig]
    dnsPolicy: core.optional[str]
    enableServiceLinks: core.optional[bool]
    ephemeralContainers: core.optional[list[io_k8s_api_core_v1_EphemeralContainer]]
    hostAliases: core.optional[list[io_k8s_api_core_v1_HostAlias]]
    hostIPC: core.optional[bool]
    hostNetwork: core.optional[bool]
    hostPID: core.optional[bool]
    hostUsers: core.optional[bool]
    hostname: core.optional[str]
    imagePullSecrets: core.optional[list[io_k8s_api_core_v1_LocalObjectReference]]
    initContainers: core.optional[list[io_k8s_api_core_v1_Container]]
    nodeName: core.optional[str]
    nodeSelector: core.optional[dict[str, str]]
    os: core.optional[io_k8s_api_core_v1_PodOS]
    overhead: core.optional[dict[str, str]]
    preemptionPolicy: core.optional[str]
    priority: core.optional[int]
    priorityClassName: core.optional[str]
    readinessGates: core.optional[list[io_k8s_api_core_v1_PodReadinessGate]]
    resourceClaims: core.optional[list[io_k8s_api_core_v1_PodResourceClaim]]
    restartPolicy: core.optional[str]
    runtimeClassName: core.optional[str]
    schedulerName: core.optional[str]
    schedulingGates: core.optional[list[io_k8s_api_core_v1_PodSchedulingGate]]
    securityContext: core.optional[io_k8s_api_core_v1_PodSecurityContext]
    serviceAccount: core.optional[str]
    serviceAccountName: core.optional[str]
    setHostnameAsFQDN: core.optional[bool]
    shareProcessNamespace: core.optional[bool]
    subdomain: core.optional[str]
    terminationGracePeriodSeconds: core.optional[int]
    tolerations: core.optional[list[io_k8s_api_core_v1_Toleration]]
    topologySpreadConstraints: core.optional[
        list[io_k8s_api_core_v1_TopologySpreadConstraint]
    ]
    volumes: core.optional[list[io_k8s_api_core_v1_Volume]]


@core.schema
class io_k8s_api_core_v1_PodTemplateSpec:
    """PodTemplateSpec describes the data a pod should have when created from a template"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.PodSpec']"""
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_PodSpec]


@core.schema
class io_k8s_api_core_v1_ReplicationControllerSpec:
    """ReplicationControllerSpec is the specification of a replication controller."""

    """Dependencies: ['io.k8s.api.core.v1.PodTemplateSpec']"""
    minReadySeconds: core.optional[int]
    replicas: core.optional[int]
    selector: core.optional[dict[str, str]]
    template: core.optional[io_k8s_api_core_v1_PodTemplateSpec]


@core.schema
class io_k8s_api_apps_v1_DaemonSetSpec:
    """DaemonSetSpec is the specification of a daemon set."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.core.v1.PodTemplateSpec', 'io.k8s.api.apps.v1.DaemonSetUpdateStrategy']"""
    minReadySeconds: core.optional[int]
    revisionHistoryLimit: core.optional[int]
    selector: io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector
    template: io_k8s_api_core_v1_PodTemplateSpec
    updateStrategy: core.optional[io_k8s_api_apps_v1_DaemonSetUpdateStrategy]


@core.schema
class io_k8s_api_apps_v1_DeploymentSpec:
    """DeploymentSpec is the specification of the desired behavior of the Deployment."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.apps.v1.DeploymentStrategy', 'io.k8s.api.core.v1.PodTemplateSpec']"""
    minReadySeconds: core.optional[int]
    paused: core.optional[bool]
    progressDeadlineSeconds: core.optional[int]
    replicas: core.optional[int]
    revisionHistoryLimit: core.optional[int]
    selector: io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector
    strategy: core.optional[io_k8s_api_apps_v1_DeploymentStrategy]
    template: io_k8s_api_core_v1_PodTemplateSpec


@core.schema
class io_k8s_api_apps_v1_ReplicaSetSpec:
    """ReplicaSetSpec is the specification of a ReplicaSet."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.core.v1.PodTemplateSpec']"""
    minReadySeconds: core.optional[int]
    replicas: core.optional[int]
    selector: io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector
    template: core.optional[io_k8s_api_core_v1_PodTemplateSpec]


@core.schema
class io_k8s_api_apps_v1_StatefulSetSpec:
    """A StatefulSetSpec is the specification of a StatefulSet."""

    """Dependencies: ['io.k8s.api.apps.v1.StatefulSetOrdinals', 'io.k8s.api.apps.v1.StatefulSetPersistentVolumeClaimRetentionPolicy', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.core.v1.PodTemplateSpec', 'io.k8s.api.apps.v1.StatefulSetUpdateStrategy', 'io.k8s.api.core.v1.PersistentVolumeClaim']"""
    minReadySeconds: core.optional[int]
    ordinals: core.optional[io_k8s_api_apps_v1_StatefulSetOrdinals]
    persistentVolumeClaimRetentionPolicy: core.optional[
        io_k8s_api_apps_v1_StatefulSetPersistentVolumeClaimRetentionPolicy
    ]
    podManagementPolicy: core.optional[str]
    replicas: core.optional[int]
    revisionHistoryLimit: core.optional[int]
    selector: io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector
    serviceName: str
    template: io_k8s_api_core_v1_PodTemplateSpec
    updateStrategy: core.optional[io_k8s_api_apps_v1_StatefulSetUpdateStrategy]
    volumeClaimTemplates: core.optional[list[io_k8s_api_core_v1_PersistentVolumeClaim]]


@core.schema
class io_k8s_api_batch_v1_JobSpec:
    """JobSpec describes how the job execution will look like."""

    """Dependencies: ['io.k8s.api.batch.v1.PodFailurePolicy', 'io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector', 'io.k8s.api.batch.v1.SuccessPolicy', 'io.k8s.api.core.v1.PodTemplateSpec']"""
    activeDeadlineSeconds: core.optional[int]
    backoffLimit: core.optional[int]
    backoffLimitPerIndex: core.optional[int]
    completionMode: core.optional[str]
    completions: core.optional[int]
    managedBy: core.optional[str]
    manualSelector: core.optional[bool]
    maxFailedIndexes: core.optional[int]
    parallelism: core.optional[int]
    podFailurePolicy: core.optional[io_k8s_api_batch_v1_PodFailurePolicy]
    podReplacementPolicy: core.optional[str]
    selector: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_LabelSelector]
    successPolicy: core.optional[io_k8s_api_batch_v1_SuccessPolicy]
    suspend: core.optional[bool]
    template: io_k8s_api_core_v1_PodTemplateSpec
    ttlSecondsAfterFinished: core.optional[int]


@core.schema
class io_k8s_api_batch_v1_JobTemplateSpec:
    """JobTemplateSpec describes the data a Job should have when created from a template"""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.batch.v1.JobSpec']"""
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_batch_v1_JobSpec]


@core.schema
class io_k8s_api_core_v1_Pod:
    """Pod is a collection of containers that can run on a host. This resource is created by clients and scheduled onto hosts."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.PodSpec', 'io.k8s.api.core.v1.PodStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_PodSpec]
    status: core.optional[io_k8s_api_core_v1_PodStatus]


@core.schema
class io_k8s_api_core_v1_PodList:
    """PodList is a list of Pods."""

    """Dependencies: ['io.k8s.api.core.v1.Pod', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_Pod]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_PodTemplate:
    """PodTemplate describes a template for creating copies of a predefined pod."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.PodTemplateSpec']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    template: core.optional[io_k8s_api_core_v1_PodTemplateSpec]


@core.schema
class io_k8s_api_core_v1_PodTemplateList:
    """PodTemplateList is a list of PodTemplates."""

    """Dependencies: ['io.k8s.api.core.v1.PodTemplate', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_PodTemplate]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_core_v1_ReplicationController:
    """ReplicationController represents the configuration of a replication controller."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.core.v1.ReplicationControllerSpec', 'io.k8s.api.core.v1.ReplicationControllerStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_core_v1_ReplicationControllerSpec]
    status: core.optional[io_k8s_api_core_v1_ReplicationControllerStatus]


@core.schema
class io_k8s_api_core_v1_ReplicationControllerList:
    """ReplicationControllerList is a collection of replication controllers."""

    """Dependencies: ['io.k8s.api.core.v1.ReplicationController', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_core_v1_ReplicationController]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_apps_v1_DaemonSet:
    """DaemonSet represents the configuration of a daemon set."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.apps.v1.DaemonSetSpec', 'io.k8s.api.apps.v1.DaemonSetStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_apps_v1_DaemonSetSpec]
    status: core.optional[io_k8s_api_apps_v1_DaemonSetStatus]


@core.schema
class io_k8s_api_apps_v1_DaemonSetList:
    """DaemonSetList is a collection of daemon sets."""

    """Dependencies: ['io.k8s.api.apps.v1.DaemonSet', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_apps_v1_DaemonSet]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_apps_v1_Deployment:
    """Deployment enables declarative updates for Pods and ReplicaSets."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.apps.v1.DeploymentSpec', 'io.k8s.api.apps.v1.DeploymentStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_apps_v1_DeploymentSpec]
    status: core.optional[io_k8s_api_apps_v1_DeploymentStatus]


@core.schema
class io_k8s_api_apps_v1_DeploymentList:
    """DeploymentList is a list of Deployments."""

    """Dependencies: ['io.k8s.api.apps.v1.Deployment', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_apps_v1_Deployment]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_apps_v1_ReplicaSet:
    """ReplicaSet ensures that a specified number of pod replicas are running at any given time."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.apps.v1.ReplicaSetSpec', 'io.k8s.api.apps.v1.ReplicaSetStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_apps_v1_ReplicaSetSpec]
    status: core.optional[io_k8s_api_apps_v1_ReplicaSetStatus]


@core.schema
class io_k8s_api_apps_v1_ReplicaSetList:
    """ReplicaSetList is a collection of ReplicaSets."""

    """Dependencies: ['io.k8s.api.apps.v1.ReplicaSet', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_apps_v1_ReplicaSet]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_apps_v1_StatefulSet:
    """StatefulSet represents a set of pods with consistent identities. Identities are defined as:
      - Network: A single stable DNS and hostname.
      - Storage: As many VolumeClaims as requested.

    The StatefulSet guarantees that a given network identity will always map to the same storage identity.
    """

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.apps.v1.StatefulSetSpec', 'io.k8s.api.apps.v1.StatefulSetStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_apps_v1_StatefulSetSpec]
    status: core.optional[io_k8s_api_apps_v1_StatefulSetStatus]


@core.schema
class io_k8s_api_apps_v1_StatefulSetList:
    """StatefulSetList is a collection of StatefulSets."""

    """Dependencies: ['io.k8s.api.apps.v1.StatefulSet', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_apps_v1_StatefulSet]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_batch_v1_CronJobSpec:
    """CronJobSpec describes how the job execution will look like and when it will actually run."""

    """Dependencies: ['io.k8s.api.batch.v1.JobTemplateSpec']"""
    concurrencyPolicy: core.optional[str]
    failedJobsHistoryLimit: core.optional[int]
    jobTemplate: io_k8s_api_batch_v1_JobTemplateSpec
    schedule: str
    startingDeadlineSeconds: core.optional[int]
    successfulJobsHistoryLimit: core.optional[int]
    suspend: core.optional[bool]
    timeZone: core.optional[str]


@core.schema
class io_k8s_api_batch_v1_Job:
    """Job represents the configuration of a single job."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.batch.v1.JobSpec', 'io.k8s.api.batch.v1.JobStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_batch_v1_JobSpec]
    status: core.optional[io_k8s_api_batch_v1_JobStatus]


@core.schema
class io_k8s_api_batch_v1_JobList:
    """JobList is a collection of jobs."""

    """Dependencies: ['io.k8s.api.batch.v1.Job', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_batch_v1_Job]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]


@core.schema
class io_k8s_api_batch_v1_CronJob:
    """CronJob represents the configuration of a single cron job."""

    """Dependencies: ['io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta', 'io.k8s.api.batch.v1.CronJobSpec', 'io.k8s.api.batch.v1.CronJobStatus']"""
    apiVersion: core.optional[str]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ObjectMeta]
    spec: core.optional[io_k8s_api_batch_v1_CronJobSpec]
    status: core.optional[io_k8s_api_batch_v1_CronJobStatus]


@core.schema
class io_k8s_api_batch_v1_CronJobList:
    """CronJobList is a collection of cron jobs."""

    """Dependencies: ['io.k8s.api.batch.v1.CronJob', 'io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta']"""
    apiVersion: core.optional[str]
    items: list[io_k8s_api_batch_v1_CronJob]
    kind: core.optional[str]
    metadata: core.optional[io_k8s_apimachinery_pkg_apis_meta_v1_ListMeta]
