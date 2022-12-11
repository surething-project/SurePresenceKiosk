// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: pose.proto

package pt.ulisboa.tecnico.surething.pose;

public interface ValueOrBuilder extends
    // @@protoc_insertion_point(interface_extends:pt.ulisboa.tecnico.surething.pose.Value)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <pre>
   * an unsigned integer or negative integer
   * </pre>
   *
   * <code>int32 int = 1;</code>
   * @return Whether the int field is set.
   */
  boolean hasInt();
  /**
   * <pre>
   * an unsigned integer or negative integer
   * </pre>
   *
   * <code>int32 int = 1;</code>
   * @return The int.
   */
  int getInt();

  /**
   * <pre>
   * utf-8 text string
   * </pre>
   *
   * <code>string tstr = 2;</code>
   * @return Whether the tstr field is set.
   */
  boolean hasTstr();
  /**
   * <pre>
   * utf-8 text string
   * </pre>
   *
   * <code>string tstr = 2;</code>
   * @return The tstr.
   */
  java.lang.String getTstr();
  /**
   * <pre>
   * utf-8 text string
   * </pre>
   *
   * <code>string tstr = 2;</code>
   * @return The bytes for tstr.
   */
  com.google.protobuf.ByteString
      getTstrBytes();

  /**
   * <pre>
   * an unsigned integer
   * </pre>
   *
   * <code>uint32 uint = 3;</code>
   * @return Whether the uint field is set.
   */
  boolean hasUint();
  /**
   * <pre>
   * an unsigned integer
   * </pre>
   *
   * <code>uint32 uint = 3;</code>
   * @return The uint.
   */
  int getUint();

  /**
   * <pre>
   * byte string
   * </pre>
   *
   * <code>bytes bstr = 4;</code>
   * @return Whether the bstr field is set.
   */
  boolean hasBstr();
  /**
   * <pre>
   * byte string
   * </pre>
   *
   * <code>bytes bstr = 4;</code>
   * @return The bstr.
   */
  com.google.protobuf.ByteString getBstr();

  public pt.ulisboa.tecnico.surething.pose.Value.ValueCase getValueCase();
}
