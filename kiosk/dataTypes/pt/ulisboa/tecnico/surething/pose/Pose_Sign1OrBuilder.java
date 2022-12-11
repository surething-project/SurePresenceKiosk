// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: pose.proto

package pt.ulisboa.tecnico.surething.pose;

public interface Pose_Sign1OrBuilder extends
    // @@protoc_insertion_point(interface_extends:pt.ulisboa.tecnico.surething.pose.Pose_Sign1)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <pre>
   *empty_or_serialized_map of HeaderMap type - string of bytes
   * </pre>
   *
   * <code>bytes protected = 1;</code>
   * @return The protected.
   */
  com.google.protobuf.ByteString getProtected();

  /**
   * <pre>
   *header map unprotected
   * </pre>
   *
   * <code>.pt.ulisboa.tecnico.surething.pose.HeaderMap unprotected = 2;</code>
   * @return Whether the unprotected field is set.
   */
  boolean hasUnprotected();
  /**
   * <pre>
   *header map unprotected
   * </pre>
   *
   * <code>.pt.ulisboa.tecnico.surething.pose.HeaderMap unprotected = 2;</code>
   * @return The unprotected.
   */
  pt.ulisboa.tecnico.surething.pose.HeaderMap getUnprotected();
  /**
   * <pre>
   *header map unprotected
   * </pre>
   *
   * <code>.pt.ulisboa.tecnico.surething.pose.HeaderMap unprotected = 2;</code>
   */
  pt.ulisboa.tecnico.surething.pose.HeaderMapOrBuilder getUnprotectedOrBuilder();

  /**
   * <pre>
   * instead of having plaintext payload, we have an encrypted structure
   * </pre>
   *
   * <code>.pt.ulisboa.tecnico.surething.pose.Enc_Structure payload = 3;</code>
   * @return Whether the payload field is set.
   */
  boolean hasPayload();
  /**
   * <pre>
   * instead of having plaintext payload, we have an encrypted structure
   * </pre>
   *
   * <code>.pt.ulisboa.tecnico.surething.pose.Enc_Structure payload = 3;</code>
   * @return The payload.
   */
  pt.ulisboa.tecnico.surething.pose.Enc_Structure getPayload();
  /**
   * <pre>
   * instead of having plaintext payload, we have an encrypted structure
   * </pre>
   *
   * <code>.pt.ulisboa.tecnico.surething.pose.Enc_Structure payload = 3;</code>
   */
  pt.ulisboa.tecnico.surething.pose.Enc_StructureOrBuilder getPayloadOrBuilder();

  /**
   * <pre>
   * computed signature value of the payload
   * </pre>
   *
   * <code>bytes signature = 4;</code>
   * @return The signature.
   */
  com.google.protobuf.ByteString getSignature();
}
