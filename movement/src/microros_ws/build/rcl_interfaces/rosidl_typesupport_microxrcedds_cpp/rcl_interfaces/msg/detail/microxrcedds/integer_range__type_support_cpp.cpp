// generated from rosidl_typesupport_microxrcedds_cpp/resource/idl__type_support.cpp.em
// with input from rcl_interfaces:msg/IntegerRange.idl
// generated code does not contain a copyright notice
#include "rcl_interfaces/msg/detail/integer_range__rosidl_typesupport_microxrcedds_cpp.hpp"
#include "rcl_interfaces/msg/detail/integer_range__struct.hpp"

#include <limits>
#include <algorithm>
#include <stdexcept>
#include <string>
#include <cstring>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_microxrcedds_cpp/identifier.hpp"
#include "rosidl_typesupport_microxrcedds_c/message_type_support.h"
#include "rosidl_typesupport_microxrcedds_cpp/message_type_support_decl.hpp"
#include "ucdr/microcdr.h"

#define MICROXRCEDDS_PADDING sizeof(uint32_t)

// forward declaration of message dependencies and their conversion functions

namespace rcl_interfaces
{

namespace msg
{

namespace typesupport_microxrcedds_cpp
{

bool
ROSIDL_TYPESUPPORT_MICROXRCEDDS_CPP_PUBLIC_rcl_interfaces
cdr_serialize(
  const rcl_interfaces::msg::IntegerRange & ros_message,
  ucdrBuffer * cdr)
{
  (void) ros_message;
  (void) cdr;
  bool rv = false;

  // Member: from_value
  rv = ucdr_serialize_int64_t(cdr, ros_message.from_value);
  // Member: to_value
  rv = ucdr_serialize_int64_t(cdr, ros_message.to_value);
  // Member: step
  rv = ucdr_serialize_uint64_t(cdr, ros_message.step);

  return rv;
}

bool
ROSIDL_TYPESUPPORT_MICROXRCEDDS_CPP_PUBLIC_rcl_interfaces
cdr_deserialize(
  ucdrBuffer * cdr,
  rcl_interfaces::msg::IntegerRange & ros_message)
{
  (void) cdr;
  (void) ros_message;
  bool rv = false;

  // Member: from_value
  rv = ucdr_deserialize_int64_t(cdr, &ros_message.from_value);
  // Member: to_value
  rv = ucdr_deserialize_int64_t(cdr, &ros_message.to_value);
  // Member: step
  rv = ucdr_deserialize_uint64_t(cdr, &ros_message.step);

  return rv;
}

size_t
ROSIDL_TYPESUPPORT_MICROXRCEDDS_CPP_PUBLIC_rcl_interfaces
get_serialized_size(
  const rcl_interfaces::msg::IntegerRange & ros_message,
  size_t current_alignment)
{
  (void) current_alignment;
  (void) ros_message;

  const size_t initial_alignment = current_alignment;

  // Member: from_value
  {
    const size_t item_size = sizeof(ros_message.from_value);
    current_alignment += ucdr_alignment(current_alignment, item_size) + item_size;
  }
  // Member: to_value
  {
    const size_t item_size = sizeof(ros_message.to_value);
    current_alignment += ucdr_alignment(current_alignment, item_size) + item_size;
  }
  // Member: step
  {
    const size_t item_size = sizeof(ros_message.step);
    current_alignment += ucdr_alignment(current_alignment, item_size) + item_size;
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_MICROXRCEDDS_CPP_PUBLIC_rcl_interfaces
max_serialized_size_IntegerRange(
  bool * full_bounded,
  size_t current_alignment)
{
  (void) current_alignment;
  *full_bounded = true;

  const size_t initial_alignment = current_alignment;

  // Member: from_value
  current_alignment += ucdr_alignment(current_alignment, sizeof(int64_t)) + sizeof(int64_t);
  // Member: to_value
  current_alignment += ucdr_alignment(current_alignment, sizeof(int64_t)) + sizeof(int64_t);
  // Member: step
  current_alignment += ucdr_alignment(current_alignment, sizeof(uint64_t)) + sizeof(uint64_t);

  return current_alignment - initial_alignment;
}

static bool _IntegerRange__cdr_serialize(
  const void * untyped_ros_message,
  ucdrBuffer * cdr)
{
  auto typed_message =
    static_cast<const rcl_interfaces::msg::IntegerRange *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _IntegerRange__cdr_deserialize(
  ucdrBuffer * cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<rcl_interfaces::msg::IntegerRange *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _IntegerRange__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const rcl_interfaces::msg::IntegerRange *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _IntegerRange__get_serialized_size_with_initial_alignment(
  const void * untyped_ros_message, size_t current_alignment)
{
  auto typed_message =
    static_cast<const rcl_interfaces::msg::IntegerRange *>(
    untyped_ros_message);
  return static_cast<size_t>(get_serialized_size(*typed_message, current_alignment));
}

static size_t _IntegerRange__max_serialized_size()
{
  bool full_bounded;
  return max_serialized_size_IntegerRange(&full_bounded, 0);
}

static message_type_support_callbacks_t _IntegerRange__callbacks = {
  "rcl_interfaces::msg",
  "IntegerRange",
  _IntegerRange__cdr_serialize,
  _IntegerRange__cdr_deserialize,
  _IntegerRange__get_serialized_size,
  _IntegerRange__get_serialized_size_with_initial_alignment,
  _IntegerRange__max_serialized_size
};

static rosidl_message_type_support_t _IntegerRange__handle = {
  rosidl_typesupport_microxrcedds_cpp::typesupport_identifier,
  &_IntegerRange__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_microxrcedds_cpp

}  // namespace msg

}  // namespace rcl_interfaces

namespace rosidl_typesupport_microxrcedds_cpp
{

template<>
ROSIDL_TYPESUPPORT_MICROXRCEDDS_CPP_EXPORT_rcl_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<rcl_interfaces::msg::IntegerRange>()
{
  return &rcl_interfaces::msg::typesupport_microxrcedds_cpp::_IntegerRange__handle;
}

}  // namespace rosidl_typesupport_microxrcedds_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_microxrcedds_cpp, rcl_interfaces, msg, IntegerRange)() {
  return &rcl_interfaces::msg::typesupport_microxrcedds_cpp::_IntegerRange__handle;
}

#ifdef __cplusplus
}
#endif
